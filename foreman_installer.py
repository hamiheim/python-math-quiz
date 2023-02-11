#!/usr/bin/env python3

# Script to install Foreman server. Work is in progress for both connected
# and disconnected installation.
# Specifically targeting EL8 for repo constraints
# Currently does not log to a file, so logging must be done manually from shell

import os
from sys import exit
from multiprocessing import cpu_count
import platform
import socket
import subprocess
import dns.resolver
import dns.reversename


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

# Define CPU core count and memory
cpuc = int(cpu_count())
memc = int(round(os.sysconf('SC_PAGE_SIZE') *
                 os.sysconf('SC_PHYS_PAGES') / 1024000000))


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


def katello_install(loc, org, badmun):
    subprocess.run(["sudo", "foreman-installer", "--scenario", "katello",
                    "--foreman-initial-location", loc,
                    "--foreman-initial-organization", org,
                    "--foreman-initial-admin-username", badmun])


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
    # Validate physical resources meet default tuning spec
    if cpuc >= 4 and memc >= 20:
        pass
    else:
        # Remember to change from fail to warn once section below is enabled
        print(f"{tcolor.flb}Host does not meeting minimum resources spec" +
              "for the default tuning profile (4 core, 20 GB Memory)")
        print(f"{tcolor.fl}Exiting!{tcolor.dflt}")
        print('')
        # print(f"{tcolor.msg}For dev deployment, set tuning to 'development'")
        # print(f"{tcolor.pmt}Development deployment?{tcolor.dflt}")
        # uans = str(input("(Y/n): "))
        # if str.lower(uans) == str("y") or str.lower(uans) == ("yes"):
        #     print('')
        #     print(f"{tcolor.okb}Proceeding with install!{tcolor.dflt}")
        #     tunp = "development"
        #     print('')
        # elif str.lower(uans) == str("n") or str.lower(uans) == ("no"):
        #     print('')
        #     print(f"{tcolor.flb}Host does not meet resource spec!")
        #     print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
        #     print('')
        #     exit()
        # else:
        #     print('')
        #     print(f"{tcolor.fl}Invalid input. Assuming no...")
        #     print('')
        #     print(f"{tcolor.flb}Host does not meet resource spec!")
        #     print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
        #     print('')
        #     exit()


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

# Check if session is "screen"ed or "tmux"ed
# If not, prompt user to continue at own risk
ptyv = os.environ['TERM']
if str(ptyv) == str("screen"):
    pass
else:
    print(f"{tcolor.wrnb}Session does not appear to be running in" +
          " asynchronous method (i.e screen or tmux)")
    print(f"{tcolor.msg}Foreman installation can be time consuming")
    print("It may not finish before remote session reaches idle timeout.")
    print('')
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

# Check if system has internet access to pull packages
# Still working on disconnected installation pieces
print(f"{tcolor.pmt}Does this host have access to online repos?{tcolor.dflt}")
uans = str(input("(Y/n): "))
if str.lower(uans) == str("y") or str.lower(uans) == ("yes"):
    print('')
    print(f"{tcolor.okb}Proceeding with install!{tcolor.dflt}")
    print('')
elif str.lower(uans) == str("n") or str.lower(uans) == ("no"):
    print('')
    print(f"{tcolor.flb}Script is not setup for disconnected installs")
    print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
    print('')
    exit()
else:
    print('')
    print(f"{tcolor.fl}Invalid input. Assuming no...")
    print(f"{tcolor.flb}Script is not setup for disconnected installs")
    print('')
    print(f"{tcolor.fl}Exiting...{tcolor.dflt}")
    print('')
    exit()

# Prompt user for targeted versions
print(f"{tcolor.pmt}What version of Foreman and Katello" +
      " are you targeting?")
print('')
print(f"{tcolor.msg}For a list of support versions, browse to:{tcolor.dflt}")
print("https://docs.theforeman.org")
print('')

while True:
    try:
        fver = float(input(tcolor.pmt + "Foreman: " + tcolor.dflt))
        break
    except ValueError:
        print(f"{tcolor.fl}Invalid input!{tcolor.dflt}")

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

# Define paramters for Foreman installation
print('')
org = input(tcolor.pmt + "Organization: " + tcolor.dflt)
loc = input(tcolor.pmt + "Location: " + tcolor.dflt)
badmun = input(tcolor.pmt + "Admin username: " + tcolor.dflt)
print('')

# Prompt user to continue with install
print(f"{tcolor.msg}Host is ready for Foreman Installation.")
print(f"{tcolor.pmt}Would you like to proceed?{tcolor.dflt}")
uans = str(input("(Y/n): "))
if str.lower(uans) == str("y") or str.lower(uans) == ("yes"):
    print('')
    print(f"{tcolor.okb}Proceeding with Foreman Installation!{tcolor.dflt}")
    print('')

    print(f"{tcolor.msg}Opening firewall for required services{tcolor.dflt}")
    enable_fw_svc("foreman")
    enable_fw_svc("foreman-proxy")
    fw_reload()

    # Had to remove logic for successful installation since Foreman
    # doesn't send a clean exit code (0) after successful install.
    # Will revist once the exit code received for both successful
    # and failed installations have been identified.
    print('')
    print(f"{tcolor.msg}Installing Foreman and Katello services{tcolor.dflt}")
    katello_install(loc, org, badmun)
    print(f"{tcolor.okb}Foreman installation complete!{tcolor.dflt}")
    log = "/var/log/foreman-installer/katello.log"
    print(f"{tcolor.gen}See :{tcolor.dflt}")
    print('')
    print("-" * len(log) + len("|  |"))
    print(f"| {log} |")
    print("-" * len(log) + len("|  |"))
    print('')
    print(f"{tcolor.gen}for detailed installation log.")
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
    print(f"{tcolor.dflt}foreman-installer --scenario katello \\")
    print(f" --foreman-initial-location={org} \\")
    print(f" --foreman-initial-organization={loc} \\")
    print(f" --foreman-initial-admin-username={badmun}")
    print('')
