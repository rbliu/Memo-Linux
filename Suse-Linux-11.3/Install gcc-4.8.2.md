Machine Factors:

Name: "Boab"

OS: SUSE Linux 11.3 (Kernel Linux 2.6.34, 64-bit)

CPU: Intel Core2 Quad Q6600 @2.40GHz

RAM: 3.2GB

The gcc version is too old. So we need to install a newer version such that we can install Sextractor later. According to the offical documentations, LSST DM Stack is built with gcc 4.8. So that is the version I will install.

Make sure you have super user permission:
```
$ su

$ mkdir /usr/local/tmp  #make this directory if there is not

$ cd /usr/local/tmp

$ wget https://ftp.gnu.org/gnu/gcc/gcc-4.8.2/gcc-4.8.2.tar.gz

$ tar -xzvf gcc-4.8.2.tar.gz

$ cd gcc-4.8.2
```
You will need some dependencies before installing gcc, this trick will help you to download them, aka gmp-4.3.2, mpc-0.8.1, and mpfr-2.4.2:
```
$ ./contrib/download_prerequistes

$ cd ..
```
Just to build gcc in a separate directory such that we don't have to worry about messing up the source directory:
```
$ mkdir gcc-build-4.8.2  

$ cd gcc-build-4.8.2
```
Now, we are ready to configure. Choose the languages that you need. Fortran is required to build Sextractor.
```
$ ../gcc-4.8.2/configure --prefix=/usr/local --enable-checking=release --enable-languages=c,c++,fortran --disable-multilib

$ make -j4
```
Because this is a quad-core machine, otherwise just make
```
$ make install
```
OK, now gcc 4.8.2 is under /usr/local/bin. If the old version is installed in /usr/bin, it may happens that the system still recognize that version. You can either remove it, or modify the environment variables:
```
$ export PATH=/usr/local/bin:$PATH
```
Also, I found it necessary to modify the path to LD lib and c++ include:
```
$ export LD_LIBRARY_PATH=/usr/local/lib64  
```
This can be /usr/local/lib, depends on where your libgfortran.so.3 is.
```
$ export CPLUS_INCLUDE_PATH=/usr/local/include/c++/4.8.2:/usr/local/include/c++/4.8.2/x86_64-unknown-linux-gnu
```
OK, now you can check the version of your gcc:
```
$ gcc --version
```
