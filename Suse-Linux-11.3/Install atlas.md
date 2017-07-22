Machine Factors:

Name: "Boab"

OS: SUSE Linux 11.3 (Kernel Linux 2.6.34, 64-bit)

CPU: Intel Core2 Quad Q6600 @2.40GHz

RAM: 3.2GB

ATLAS is prerequested by Sextractor. You only need to install atlas development package. But I suggest to install the full atlas package.

Remember that building ATLAS requires gcc 4.7 or above.

Here I will install atlas-3.10.2 and lapack-3.4.1:

$ su

First you need to turn off the CPU throttling:

If you are using CentOS 6, it is simple:

$ /usr/bin/cpufreq-selector -g performance

If you are using SUSE like me, you need to select "cpufrequtils" in YaST software management, and

$ /usr/bin/cpufreq-set -g performance

If you are using a laptop, I suggest to change it back after installing ATLAS:

$ /usr/bin/cpufreq-set -g ondemand

Good, now we can download and install ATLAS:

$ cd /usr/local/tmp

$ wget http://fossies.org/linux/misc/atlas3.10.2.tar.gz

$ wget http://www.netlib.org/lapack/lapack-3.4.1.tgz

$ tar -xzvf atlas3.10.2.tar.gz

$ mv ATLAS ATLAS3.10.2

$ mkdir atlas-build

$ cd atlas-build

$ ../ATLAS3.10.2/configure -b 64 -D c -DPentiumCPS=2400 --prefix=/usr/local --incdir=/usr/local/include --libdir=/usr/local/lib --with-netlib-lapack-tarfile=/usr/local/tmp/lapack-3.4.1.tgz

In the above command, "-b 64" means the OS is 64-bit; "-D c -DPentiumCPS=2400" set my CPU frequency as 2400MHz which is the max value for my computer.

$ make build  # tune & build lib

$ make check  # sanity check correct answer

You may see this output: make[1]: [sanity_test] Error 1 (ignored). But it is just fine.

$ make ptcheck  # sanity check parallel

$ make time  # check if lib is fast

$ make install  # copy libs to install dir

Now you can find atlas library and include files under /usr/local/lib and /usr/local/include
