Machine Factors:

Name: `ghk1`

OS: Scientific Linux release 6.9 (Carbon)(Linux 2.6.32, 64-bit)

CPU: Intel(R) Xeon(R) CPU E5-2687W 0 @ 3.10GHz (2 threads/core x 32 cores)

RAM: 66GB

The original gcc version (4.4.7) is too old. So we need to install a newer version such that we can install DM Stack later. According to the offical documentations, LSST DM Stack is built with gcc 4.8. So that is the version I will install.

Make sure you have super user permission:
```
su
```

Add the YUM repositories:
```
sudo wget -O /etc/yum.repos.d/slc6-devtoolset.repo \
  http://linuxsoft.cern.ch/cern/devtoolset/slc6-devtoolset.repo
wget -O /etc/yum.repos.d/slc5-devtoolset.repo \
  http://linuxsoft.cern.ch/cern/devtoolset/slc5-devtoolset.repo
```

Install devtoolset-2 via YUM:
```
yum install devtoolset-2
```

OK, now `gcc-4.8.2` is under `/opt/rh/devtoolset-2/root/usr/bin`. If the old version is installed in `/usr/bin`, it may happens that the system still recognize that version. You can either remove it, or modify the environment variables:
```
export PATH=/opt/rh/devtoolset-2/root/usr/bin:$PATH
```

Also, I found it necessary to modify the path to LD lib and c++ include:
OK, now you can check the version of your gcc:
```
gcc --version
gcc (GCC) 4.8.2 20140120 (Red Hat 4.8.2-15)
Copyright (C) 2013 Free Software Foundation, Inc.
```
