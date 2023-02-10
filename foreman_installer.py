#!/usr/env/python3

# Script to install Foreman server. Work is in progress for both connected
# and disconnected installation methodsself.
# Specifically targeting EL8 for repo constraints

import os
import platform
import socket
import subprocess

red = '\033[1;31m'
lrd = '\033[0;31m'
cyn = '\033[1;36m'
lcn = '\033[0;36m'
ylow = '\033[1;33m'
grn = '\033[1;32m'
prpl = '\033[1;35m'
nclr = '\033[0m'

LOG = "/tmp/foreman-install.log"

hname = socket.gethostname()
ipaddr = socket.gethostbyname(socket.gethostname())


def clear_screen():
    os.system('clear')


clear_screen()


# Check platform ID
def platform_id():
    try:
        if relid.index("el8"):
            pass
    except ValueError:
        print("EL8 platform not deteced! Exiting!")
        quit()


# Get host release info
relid = platform.release()

banner = "# Foreman Installation Script #"
print('')
print("-" * len(banner))
print(banner)
print("-" * len(banner))
print('')

platform_id()

# Check if session is "screen"ed or "tmux"ed
#ptyv=$(echo $TERM 2>/dev/null)
#if [[ $ptyv == screen ]]
#then :
#else
#  echo -e $yellow"\nSession does not appear to be running in an asynchronous method (i.e screen or tmux)"$ncolor
#  echo -e $lcyan"\nForeman installation can be time consuming, and may not finish before an idle timeout is reached for remote sessions."
#  echo -e $cyan"\nDo you wish to proceed?"
#  read yn
#  while true
#  do
#    case $yn in
#      [Yy]) echo -e $yellow"\nProceeding without screen/tmux"$nocolor
#        break;;
#      [Nn]) echo -e $red"\nExiting!"$ncolor
#        exit;
#        break;;
#      *) echo -e $lred"\nInvalid Input!"$nocolor
#    esac
#  done
#fi
#
#if grep $hname /etc/hosts || nslookup $ipaddr 1>/dev/null;
#then :
#else
#  echo -e $red"\nReverse DNS failed! Configure hosts file with the following entry:"$ncolor
#  echo -e "$hname  $ipaddr\n"
#  echo -e $purple"\nDetails can be found in $LOG and /var/log/foreman-installer"$ncolor
#  exit
#fi
#
#echo -e $cyan"\nIs this a disconnected environment?"$ncolor
#read yn
#while true
#do
#  case $yn in 
#    [Yy]) echo -e $red"\nScript is not configured to handle disconnected systems yet. Sorry"
#      echo -e $lred"\nExiting..."$ncolor; exit;;
#    [Nn]) echo -e $green"\nContinuing with online installation..."$ncolor
#      break;;
#    *) echo -e $lred"\nInvalid input!"$ncolor
#  esac
#done
#
#echo -e $cyan"\nWhat version of Foreman are you targeting?"$ncolor
#echo -e $lcyan"If unknown, browse to $ncolor docs.theforeman.org $lcyan for current supported release versions"$ncolor
#read fver
#
#echo -e $cyan"\nWhat version of Katello are you targeting?"$ncolor
#read kver
#
#echo -e $lcyan"\nConfiguring repositories..."$purple
#sudo dnf install -y https://yum.theforeman.org/releases/$fver/el8/x86_64/foreman-release.rpm
#sudo dnf install -y https://yum.theforeman.org/katello/$kver/katello/el8/x86_64/katello-repos-latest.rpm
#sudo dnf install -y https://yum.puppet.com/puppet7-release-el-8.noarch.rpm
#sudo dnf module -y disable postgresql:10
#sudo dnf module -y enable postgresql:12
#sudo dnf module -y disable ruby:2.5
#sudo dnf module -y enable ruby:2.7
#sudo dnf module -y enable katello:el8 pulpcore:el8
#sudo dnf repolist --enablerepo={appstream,baseos} &>/dev/null
#
#echo -e $lcyan"\nInstalling packages..."$purple
#sudo dnf update -y
#sudo dnf install foreman-installer-katello -y
#
#echo -e $green"\nPackage installation complete."
#echo -e $lcyan"\nRun $ncolor rpm -qa kernel --last $lcyan to see if a reboot is needed."$ncolor
#
#echo -e $cyan"\nHost is ready for Foreman installation. Would you like to proceed?"$ncolor
#read yn
#while true
#do
#  case $yn in
#    [Yy]) echo -e $green"\nProceeding with Foreman Installation!\n"$ncolor
#      echo -e $cyan"\nName of organization?"$ncolor
#      read org
#      echo -e $cyan"\nName of location?"$ncolor
#      read loc
#      echo -e $cyan"\nBuilt-in administrator username?"$ncolor
#      read badmun
#      if sudo foreman-installer --scenario katello --foreman-initial-location="$loc" --foreman-initial-organization="org" --foreman-initial-admin-username="$badmun"
#      then
#        echo -e $green"\nForeman Installation complete!"
#        echo -e "Browse to https://$hname:443 to peform site configurations"$nocolor
#      else
#        echo -e $red"\nForeman Installation failed!"$ncolor
#      fi
#      break;;
#    [Nn]) echo -e $yellow"\nPackage installation complete but Foreman has not been installed"
#      echo -e $lcyan"Execute 'foreman-installer --scenario katello' to complete installation."$ncolor
#      break;;
#    *) echo -e $lred"\nInvalid input!"$ncolor
#  esac
#done
#
#sed -i '/Initial credentials are/c\      {{ Initial credentials have been redacted }}' /tmp/foreman-install.log
#
#echo -e $purple"\nDetails can be found in $LOG and /var/log/foreman-installer"$ncolor
