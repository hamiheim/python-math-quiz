#!/usr/bin/env python3

# Script to install Foreman server. Work is in progress for both connected
# and disconnected installation.
# Specifically targeting EL8 for repo constraints
# Currently does not log to a file, so logging must be done manually from shell

import os
from sys import exit
from multiprocessing import cpu_count
import psutil
import platform
import argparse
import socket
import subprocess
import dns.resolver
import dns.reversename

# Define arguements for script
arg = argparse.ArgumentParser(description="Foreman installer script",
                              formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg.add_argument("-a", "--noprompt", action="store_true",
                 help="Do not prompt to continue/on non-critical errors")
arg.add_argument("-d", "--discon", action="store_true",
                 help="Disconnected mode")
arg.add_argument("-f", "--foreman", action="store",
                 help="Foreman version", default="")
arg.add_argument("-k", "--katello", action="store",
                 help="Katello version", default="")
arg.add_argument("-l", "--loc", action="store", help="Location",
                 default="Default_Location")
arg.add_argument("-o", "--org", action="store",
                 help="Organization", default="Default_Organization")
arg.add_argument("-t", "--tune", action="store",
                 help="Tuning profile. Acceptable options include:" +
                 " default, medium, large, extra-large, extra-extra-large",
                 default="default")
arg.add_argument("-u", "--username", action="store",
                 help="Admin username", default="admin")

arg.add_argument("-c", "--compute-resource", dest="compute_resource",
                 action="store", help="Compute Resource type")

# Virtualization --> Installer argument
# Amazon EC2 --> --enable-foreman-compute-ec2
# Google Compute Engine --> --enable-foreman-compute-gce
# Libvirt --> --enable-foreman-compute-libvirt
# openstack --> --enable-foreman-compute-openstack
# oVirt / RHV --> --enable-foreman-compute-ovirt
# VMware --> t u--enable-foreman-compute-vmware

arg.add_argument("--cr-username", dest="cr_username", action="store",
                 help="Compute Resource username")

arg.add_argument("--cr-password", dest="cr_password", action="store",
                 help="Compute Resource password")

arg.add_argument("--cr-server", dest="cr_server", action="store",
                 help="Compute Resource server")

arg.add_argument("--cr-datacenter", dest="cr_datacenter", action="store",
                 help="Compute Resource Datacenter")

flg = arg.parse_args()

if flg.cr_username and not flg.compute_resource:
    arg.error("--cr-username requires --compute-resource")

if flg.cr_password and not flg.compute_resource:
    arg.error("--cr-password requires --compute-resource")

if flg.cr_server and not flg.compute_resource:
    arg.error("--cr-server requires --compute-resource")

if flg.cr_datacenter and not flg.compute_resource:
    arg.error("--cr-dataceneter requires --compute-resource")

if flg.compute_resource and not flg.cr_username or not flg.cr_password or not flg.cr_server or not flg.cr_datacenter:
    arg.error("--compute-resource requires --cr-username," +
              " --cr-password, --cr-server, and --cr-datacenter")

# Define required variables
disconnected = flg.discon
npmt = flg.noprompt
fver = flg.foreman
kver = flg.katello
tunp = flg.tune
org = flg.org
loc = flg.loc
badmun = flg.username
crpack = flg.compute_resource


# Define terminal color output variables using ANSII codes
class tcolor:
    fl = '\033[0;31m'
    flb = '\033[1;31m'
    msg = '\033[0;36m'
    pmt = '\033[1;36m'
    wrn = '\033[0;33m'
    wrnb = '\033[1;33m'
    ok = '\033[0;32m'
    okb = '\033[1;32m'
    gen = '\033[0;35m'
    dflt = '\033[0m'


# Define hostname and IP Address
hname = socket.gethostname()
ipaddr = socket.gethostbyname(socket.gethostname())


# Define required functions
def clear_screen():
    os.system('clear')


# Subprocess functions for running commands directly on the host shell
def enable_repo(repo_name):
    subprocess.run(["sudo", "dnf", "repolist", "--enablerepo", repo_name])


def install_package(package_name):
    subprocess.run(["sudo", "dnf", "install", "-y", package_name])


def update_package():
    subprocess.run(["sudo", "dnf", "update", "-y"])


def install_module(package_name):
    subprocess.run(["sudo", "dnf", "module", "install", "-y", package_name])


def enable_module(module_name):
    subprocess.run(["sudo", "dnf", "module", "enable", "-y", module_name])


def disable_module(module_name):
    subprocess.run(["sudo", "dnf", "module", "disable", "-y", module_name])


def enable_fw_svc(firewall_service):
    subprocess.run(["sudo", "firewall-cmd", "--add-service", firewall_service])


def fw_reload():
    subprocess.run(["sudo", "firewall-cmd", "--runtime-to-permanent"])


def katello_install(loc, org, badmun, tunp):
    subprocess.run(["sudo", "foreman-installer", "--scenario", "katello",
                    "--tuning", tunp,
                    "--foreman-initial-location", loc,
                    "--foreman-initial-organization", org,
                    "--foreman-initial-admin-username", badmun])


def foreman_compute(crpack):
    subprocess.run(["sudo", "foreman-maintain", "packages", "install", crpack])


def vmw_cr_setup(crun, crpw, srvr, dc):
    subprocess.run(["sudo", "hammer", "compute-resource", "create",
                    "--provider", "vmware", "--name", "VMware CR", "--user",
                    crun, "--password", crpw, "--server", srvr, "--datacenter",
                    dc])


# Section for setup of external auth source (i.e. IdM)
# def ext_auth_source():


# Check platform ID
def platform_id():
    # Get host release info
    relid = platform.release()
    try:
        if relid.index("el8"):
            pass
    except ValueError:
        print(f"{tcolor.flb}EL8 platform not detected!")
        print(f"{tcolor.fl}Exiting!{tcolor.dflt}")
        exit()


def resource_check():
    global tunp

    # Define CPU core count and memory
    cpuc = int(cpu_count())
    memc = int(round(psutil.virtual_memory().total / 1024000000))

    # Validate physical resources meet default tuning spec
    if cpuc < 4 or memc < 20:
        print(f"{tcolor.wrnb}Host does not meet minimum resources spec" +
              f" for the default tuning profile {tcolor.wrn}" +
              "(4 core, 20 GB Memory)")
        print('')
        print(f"{tcolor.msg}For dev deployment, we'll set tuning to " +
              f"{tcolor.dflt}development")
        print('')
        if npmt:
            print(f"{tcolor.wrn}Assuming dev deployment...{tcolor.dflt}")
            if memc >= 6:
                tunp = "development"
                print('')
                print(f"{tcolor.okb}Proceeding with install!{tcolor.dflt}")
                print('')
            else:
                print('')
                print(f"{tcolor.flb}Host does not meet the minimum " +
                      "resources for the development tuning profile" +
                      f"{tcolor.fl} (1 core, 6 GB Memory)")
                print(f"{tcolor.fl}Exiting!{tcolor.dflt}")
                print('')
                exit()
            print('')
        else:
            print(f"{tcolor.pmt}Is this a development " +
                  f"deployment?{tcolor.dflt}")
            uans = str(input("(Y/n): "))
            if str.lower(uans) == str("y") or str.lower(uans) == ("yes"):
                if memc >= 6:
                    tunp = "development"
                    print('')
                    print(f"{tcolor.okb}Proceeding with install!{tcolor.dflt}")
                    print('')
                else:
                    print('')
                    print(f"{tcolor.flb}Host does not meet the minimum " +
                          "resources for the development tuning profile" +
                          f"{tcolor.fl} (1 core, 6 GB Memory)")
                    print(f"{tcolor.fl}Exiting!{tcolor.dflt}")
                    print('')
                    exit()
            elif str.lower(uans) == str("n") or str.lower(uans) == ("no"):
                print('')
                print(f"{tcolor.flb}Host does not meet resource spec!")
                print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
                print('')
                exit()
            else:
                print('')
                print(f"{tcolor.fl}Invalid input. Assuming no...")
                print('')
                print(f"{tcolor.flb}Host does not meet resource spec!")
                print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
                print('')
                exit()


def foreman_install():
    global log
    global loc
    global org
    global badmun
    global tunp
    print(f"{tcolor.okb}Proceeding with Foreman Installation!{tcolor.dflt}")
    print('')

    print(f"{tcolor.msg}Opening firewall for required services{tcolor.dflt}")
    enable_fw_svc("foreman")
    enable_fw_svc("foreman-proxy")
    fw_reload()
    print('')

    # Had to remove logic for successful installation since Foreman
    # doesn't send a clean exit code (0) after successful install.
    # Will revist once the exit code received for both successful
    # and failed installations have been identified.
    print(f"{tcolor.msg}Installing Foreman and Katello services{tcolor.dflt}")
    katello_install(loc, org, badmun, tunp)
    print(f"{tcolor.okb}Foreman installation complete!{tcolor.dflt}")
    log = "/var/log/foreman-installer/katello.log"
    print(f"{tcolor.gen}See the following location for details:{tcolor.dflt}")
    print('')
    print("-" * len(log + str("|  |")))
    print(f"| {log} |")
    print("-" * len(log + str("|  |")))
    print('')


clear_screen()


# Script init banner
banner = "# Foreman Installation Script #"
print('')
print(f"{tcolor.gen}-" * len(banner))
print(f"{tcolor.gen}{banner}")
print(f"{tcolor.gen}-{tcolor.dflt}" * len(banner))
print('')

# Check platform ID to ensure it's EL8
platform_id()

# Check host resources
resource_check()

# Check if session is "screen"ed or "tmux"ed
# If not, prompt user to continue at own risk
ptyv = os.environ['TERM']
if str(ptyv) != str("screen"):
    print(f"{tcolor.wrnb}Session does not appear to be running in" +
          " asynchronous method (i.e screen or tmux)")
    print(f"{tcolor.msg}Foreman installation can be time consuming")
    print("It may not finish before remote session reaches idle timeout.")
    print('')
    if npmt:
        print(f"{tcolor.wrn}Proceeding without screen/tmux{tcolor.dflt}")
        print('')
    else:
        print(f"{tcolor.pmt}Do you wish to proceed?{tcolor.dflt}")
        uans = str(input("(Y/n): "))
        if str.lower(uans) == str("y") or str.lower(uans) == ("yes"):
            print('')
            print(f"{tcolor.wrn}Proceeding without screen/tmux{tcolor.dflt}")
        elif str.lower(uans) == str("n") or str.lower(uans) == ("no"):
            print('')
            print(f"{tcolor.flb}Exiting...{tcolor.dflt}")
            exit()
        else:
            print('')
            print(f"{tcolor.fl}Invalid input. Assuming no...")
            print(f"{tcolor.flb}Exiting...{tcolor.dflt}")
            exit()

# Validate reverse DNS record for host (required for install)
try:
    dns.resolver.query(dns.reversename.from_address(ipaddr), 'PTR')
except dns.resolver.NXDOMAIN:
    print('')
    print(f"{tcolor.flb}Reverse DNS lookup failed!{tcolor.dflt}")
    print(f"{tcolor.msg}Ensure hosts file has" +
          f" the following entry or install will fail:{tcolor.dflt}")
    print('')
    print("-" * len(hname + str('    ') + str('|  |') + ipaddr))
    print(f"| {ipaddr}    {hname} |")
    print("-" * len(ipaddr + str('    ') + str('|  |') + hname))
    print('')
    if npmt:
        print(f"{tcolor.wrn}Proceeding with install!{tcolor.dflt}")
    else:
        print(f"{tcolor.pmt}Do you wish to continue{tcolor.dflt}")
        uans = str(input("(Y/n): "))
        if str.lower(uans) == str("y") or str.lower(uans) == ("yes"):
            print('')
            print(f"{tcolor.wrn}Proceeding with install!{tcolor.dflt}")
            print('')
        elif str.lower(uans) == str("n") or str.lower(uans) == ("no"):
            print('')
            print(f"{tcolor.wrn}Submit PTR record in DNS" +
                  " server or configure hosts file with above entry")
            print('')
            print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
            print('')
            exit()
        else:
            print('')
            print(f"{tcolor.fl}Invalid input. Assuming no...")
            print(f"{tcolor.wrn}Submit PTR record in DNS" +
                  " server or configure hosts file with above entry")
            print('')
            print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
            print('')
            exit()

if disconnected:
    print(f"{tcolor.flb}Script is not yet setup for disconnected installs")
    print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
    print('')
    exit()

# Define Foreman and Katello versions
if len(fver) == 0 and npmt:
    print(f"{tcolor.flb}Unable to get Foreman verison interactively!")
    print(f"{tcolor.fl}Define foreman argument, or allow prompting")
    print(f"{tcolor.msg}Use -h or --help for assistance{tcolor.dflt}")
    print('')
    exit()
elif len(fver) == 0:
    print(f"{tcolor.pmt}What version of Foreman" +
          " are you targeting?")
    print('')
    print(f"{tcolor.msg}For a list of supported" +
          f" versions, browse to:{tcolor.dflt}")
    print("https://docs.theforeman.org")
    print('')
    while True:
        try:
            fver = float(input(tcolor.pmt + "Foreman: " + tcolor.dflt))
            break
        except ValueError:
            print(f"{tcolor.fl}Invalid input!{tcolor.dflt}")

if len(kver) == 0 and npmt:
    print(f"{tcolor.flb}Unable to get Katello verison interactively!")
    print(f"{tcolor.fl}Define Katello argument, or allow prompting")
    print(f"{tcolor.msg}Use -h or --help for assistance{tcolor.dflt}")
    print('')
    exit()
elif len(kver) == 0:
    print(f"{tcolor.pmt}What version of Katello are you targeting?")
    print('')
    print(f"{tcolor.msg}For a list of supported" +
          f" versions, browse to:{tcolor.dflt}")
    print("https://docs.theforeman.org")
    print('')
    while True:
        try:
            kver = float(input(tcolor.pmt + "Katello: " + tcolor.dflt))
            break
        except ValueError:
            print(f"{tcolor.fl}Invalid input!{tcolor.dflt}")


# Setup/install repositories required for installation
print('')
print(f"{tcolor.msg}Configuring repositories...{tcolor.dflt}")
print('')
install_package("https://yum.theforeman.org/releases/" +
                str(fver) + "/el8/x86_64/foreman-release.rpm")
install_package("https://yum.theforeman.org/katello/" + str(kver) +
                "/katello/el8/x86_64/katello-repos-latest.rpm")
install_package("https://yum.puppet.com/puppet7-release-el-8.noarch.rpm")
enable_repo("appstream")
enable_repo("baseos")
print(f"{tcolor.ok}Repositories configured!{tcolor.dflt}")
print('')

# Disabled conflicting modules, and enabled required modules for installation
# Errors may be encountered if modules are already enabled/disabled
# These can be safely ignored. I will work on error handling later
print(f"{tcolor.msg}Configuring DNF Modules...{tcolor.dflt}")
disable_module("postgresql:10")
disable_module("ruby:2.5")
enable_module("postgresql:12")
enable_module("ruby:2.7")
enable_module("katello:el8")
enable_module("pulpcore:el8")
print(f"{tcolor.ok}DNF Modules configured!{tcolor.dflt}")
print('')

# Install required packages
print(f"{tcolor.msg}Installing packages...{tcolor.dflt}")
update_package()
install_package("foreman-installer-katello")
print(f"{tcolor.ok}Package installation complete!{tcolor.dflt}")
print('')

# Part of package installation is to do a full system update
# User should reboot host if kernel was updated
print(f"{tcolor.msg}Run {tcolor.dflt}rpm -qa kernel --last{tcolor.msg}" +
      f" to see if a reboot is needed.{tcolor.dflt}")

# Define paramaters for Foreman installation
print('')
if len(org) == 0:
    org = input(tcolor.pmt + "Organization: " + tcolor.dflt)
if len(loc) == 0:
    loc = input(tcolor.pmt + "Location: " + tcolor.dflt)
if len(badmun) == 0:
    badmun = input(tcolor.pmt + "Admin username: " + tcolor.dflt)
print('')

# Prompt user to continue with install
print(f"{tcolor.msg}Host is ready for Foreman Installation.")
if npmt:
    foreman_install()
else:
    print(f"{tcolor.pmt}Would you like to proceed?{tcolor.dflt}")
    uans = str(input("(Y/n): "))
    if str.lower(uans) == str("y") or str.lower(uans) == ("yes"):
        print('')
        foreman_install()
    elif str.lower(uans) == str("n") or str.lower(uans) == ("no"):
        print('')
        print(f"{tcolor.wrn}Host is setup for Foreman installation" +
              f" but foreman has {tcolor.fl}NOT{tcolor.wrn} been installed.")
        print('')
        print(f"{tcolor.msg}Execute the following to complete installation:")
        print(f"{tcolor.dflt}firewall-cmd " +
              "--add-service={foreman,foreman-proxy}")
        print("firewall-cmd --runtime-to-permanent")
        print("foreman-installer --scenario katello \\")
        print(f" --foreman-initial-location={org} \\")
        print(f" --foreman-initial-organization={loc} \\")
        print(f" --foreman-initial-admin-username={badmun}")
        print(f'{tcolor.dflt}')
    else:
        print('')
        print(f"{tcolor.fl}Invalid input. Assuming no...")
        print(f"{tcolor.wrn}Host is setup for Foreman installation" +
              f" but foreman has {tcolor.fl}NOT{tcolor.wrn} been installed.")
        print('')
        print(f"{tcolor.msg}Execute the following to complete installation:")
        print(f"{tcolor.dflt}firewall-cmd " +
              "--add-service={foreman,foreman-proxy}")
        print("firewall-cmd --runtime-to-permanent")
        print(f"{tcolor.dflt}foreman-installer --scenario katello \\")
        print(f" --foreman-initial-location={org} \\")
        print(f" --foreman-initial-organization={loc} \\")
        print(f" --foreman-initial-admin-username={badmun}")
        print('')

if len(crpack) > 0:
    print(f"{tcolor.msg}Installing {crpack} compute resource" +
          " package{tcolor.dflt}")
    foreman_compute()
    if crpack == str("vmware"):
        vmw_cr_setup()

# Section for running auth source setup
# if len(<arg>) > 0
#   print(f"{tcolor.msg}Setting up Authentication Source{tcolor.dflt}")
#   ext_auth_source()

# Future plans
# - Add ability to specify additional plugins to enable
# - Option for setup disconnected installation media only
# - Disconnected installation
