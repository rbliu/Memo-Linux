Machine Factors:

Name: "Boab"

OS: SUSE Linux 11.3 (Kernel Linux 2.6.34, 64-bit)

CPU: Intel Core2 Quad Q6600 @2.40GHz

RAM: 3.2GB

FFTW is prerequested by Sextractor.

$ su

$ cd /usr/local/tmp

$ wget http://fftw.org/fftw-3.3.4.tar.gz

$ tar -xzvf fftw-3.3.4.tar.gz

$ cd fftw-3.3.4

$ ./configure --prefix=/usr/local --enable-float --enable-single --enable-threads --disable-fortran

$ make

$ make install

Now you can find the library and include files under /usr/local/lib and /usr/local/include
