Here is the memo I wrote when I was installing CentOS 7 on 'ash' and configuring it as an NIS client.

# Install CentOS 7 on ash

Press F2 or Del to get into BOOT. Boot from USB disk.

## Software: GNOME Desktop
* GNOME Applications
* Internet Applications
* Legacy X Window
* Office Suite
* Compatibility Lib
* Development Tools
* Security Tools

## Partition
* Device Type: Standard Partition
* FS: xfs
  * 389G ==> `/export/home`
  * 60G  ==> `/`
  * ~1G  ==> `/Boot`
  * 7.8G ==> `/var`

## Ethernet IPv4: Manual
|Address|Netmask|Gateway|
|-------|-------| -------|
|?.?.26.150|255.255.255.0|?.?.26.1|

* DNS: ?.?.26.101
* Search Domain: het.brown.edu

## BEGIN INSTALLATION!
Only set the root password. DON'T create any local user!

------

# NIS Client configuration

## Install Software

Login as root.

*	yum -y install ypbind rpcbind autofs
* Use the GUI `setup` to setup NIS domain:
```
setup
[*]Use NIS  
[*] Use MD5 Passwords  [*] Use Shadow Passwords  
[*] User Fingerprint reader  [*] Local Authorization is sufficient
Domain: hetnis
Server:?.?.26.101
```

## Disable SELinux
We do not want SELinux.
```
vim /etc/selinux/config
```
and modify the first line to `SELINUX=disabled`.

## Update files:
We also need to modify the following files in `/etc`:
```
/etc/hosts
/etc/auto.master
/etc/nsswitch
/etc/resolv.conf
/etc/yp.conf
/etc/idmap.conf

/etc/pam.d/system-auth
/etc/sysconfig/network
/etc/sysconfig/authconfig
```
It is a good idea to make a backup of `/etc` from the old system.

## Turn off NetworkManager

NetworkManager has /home open, so NIS server cannot mount `/home` to local mount point. To stop it:
```
systemctl stop NetworkManager.service
rmdir /home
systemctl kill NetworkManager.service
rmdir /home
```

## Restart the autofs service
Restart the autofs service and configure the service to start following a system reboot:
```
service autofs restart
chkconfig autofs on
```	

## Prevent GNOME initial setup
When you enter the GNOME login interface, it keeps prompting the new user creation screen. To skip this step and load users/paswords directly from NIS server:
```
echo "yes" >> /etc/skel/.config/gnome-initial-setup-done
```
And add "InitialSetupEnable=False" under [daemon] in /etc/gdm/custom.conf

------
Now, we are able to login via ssh or locally!

# Tricks
* Boot into command line: `Ctrl+Alt+F2`; back to GNOME: `Alt+right arrow`
* Remove user together with its home directory: `userdel -r USERNAME`
* List `auto.master` mappings: `ypcat -k auto.master`
* List `auto.home` account keys: `ypcat -k auto.home`

# Problem
* How to mount NIS `/home` correctly (All `/home` mounted by "nobody" instead the user)

Solved: Add "Domain = het.brown.edu" in /etc/idmap.conf
    
* How to setup ssh public key from other NIS client? (Require password anytime anywhere)

Solved: After solving the "nobody" user problem, logout & login & `cd ~/.ssh`; make sure the owner of `~/.ssh` is the correct user

# Useful Links
https://docs.oracle.com/cd/E37670_01/E41138/html/ol_cfgclnt_nis.html
https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-nfs-client-config-autofs.html
http://cn.linux.vbird.org/linux_server/0430nis_3.php
https://bugzilla.redhat.com/show_bug.cgi?id=1226819
https://seven.centos.org/2013/12/preventing-gnome3s-initial-setup/
