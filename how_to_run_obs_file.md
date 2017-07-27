#From Simon Krughoff's notes

How to run `obs_file`

* get data – here I use **filename=trial07**.fits as an example.

* get obs_file (assuming you have a stack set up)
```
git clone https://github.com/SimonKrughoff/obs_file
cd obs_file
git checkout tickets/DM-6924
setup -k -r .
scons
cd ..
```

* setup repo

make a directory to put things in – 
```
mkdir input
```

provide a mapper – 
```
echo "lsst.obs.file.FileMapper" > input/_mapper
```

* ingest the data – 
```
ingestImages.py input/ trial07.fits --mode link
```

* process the data – 
```
processCcd.py input/ --id filename=trial07.fits --config isr.noise=5 --output output
```

Note that you need to make a pretty goood guess at the noise in the image.  This is something I'd like to fix.
