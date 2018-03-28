When I was trying to install `DM-14.0` on `ghk1`, an error occured indicating that `gcc-4.8.2` does not include C++14 extension. Therefore, we need a newer version of `gcc` on `ghk1`.

Given the fact that `ghk1` is running `ScientificLinux 6.9`, I did not find an official yum source which has `DevToolSet`. So I had to add a third-party source repository.

```
su
vim /etc/yum.repos.d/CentOS-Base.repo
```

Add the following lines into this `CentOS-Base.repo` file:
```
# CentOS-Base.repo
#
# The mirror system uses the connecting IP address of the client and the
# update status of each mirror to pick mirrors that are updated to and
# geographically close to the client.  You should use this for CentOS updates
# unless you are manually picking other mirrors.
#
# If the mirrorlist= does not work for you, as a fall back you can try the
# remarked out baseurl= line instead.
#
#

[base]
name=CentOS-$releasever - Base - mirrors.ustc.edu.cn
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/os/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os
gpgcheck=1
gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

#released updates
[updates]
name=CentOS-$releasever - Updates - mirrors.ustc.edu.cn
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/updates/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates
gpgcheck=1
gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras - mirrors.ustc.edu.cn
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/extras/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras
gpgcheck=1
gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus - mirrors.ustc.edu.cn
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/centosplus/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus
gpgcheck=1
enabled=0
gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

#contrib - packages by Centos Users
[contrib]
name=CentOS-$releasever - Contrib - mirrors.ustc.edu.cn
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/contrib/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=contrib
gpgcheck=1
enabled=0
gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6
```
and save the file.

Then
```
yum repolist
yum install centos-release-scl -y
yum-config-manager --enable rhel-server-rhscl-7-rpms
yum install devtoolset-7 -y
scl enable devtoolset-7 bash
```

OK, now add `export PATH=/opt/rh/devtoolset-7/root/usr/bin:$PATH` into the `~/.bashrc` file, and it's done!


## Reference websites:
* https://www.softwarecollections.org/en/scls/rhscl/devtoolset-7/
* http://mirrors.ustc.edu.cn/help/centos.html
