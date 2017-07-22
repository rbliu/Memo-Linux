Machine Factors:

Name: "Boab"

OS: SUSE Linux 11.3 (Kernel Linux 2.6.34, 64-bit)

CPU: Intel Core2 Quad Q6600 @2.40GHz

RAM: 3.2GB

Before installing Sextractor, you should already have gcc-4.8.2, fftw-3.3.4, and atlas-3.10.2

$ su

$ cd /usr/local/tmp

$ wget http://www.astromatic.net/download/sextractor/sextractor-2.19.5.tar.gz

$ tar -xzvf sextractor-2.19.5.tar.gz

$ cd sextractor-2.19.5

$ ./configure --prefix=/usr/local/sextractor-2.19.5 --with-atlas=/usr/local/lib --with-atlas-incdir=/usr/local/include --with-fftw=/usr/local/lib --with-fftw-incdir=/usr/local/include --enable-threads

$ make

$ make install

$ ln -s /usr/local/sextractor-2.19.5/sex /usr/local/bin/sex

$ cp -rp config /usr/local/sextractor-2.19.5

Now, Sextractor-2.19.5 is installed under /usr/local/sextractor-2.19.5 and a symbolic link is created at /usr/local/bin/sex. 

To process Sextractor on one fits file, cd to the directory of the fits file and

$ sex -c ***.sex ***.fits

The *.sex file (as well as *.param, *.conv, *.psf files) should be in the same directory.
