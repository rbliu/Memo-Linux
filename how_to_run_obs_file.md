*From Simon Krughoff's notes*

How to run [`obs_file`](https://github.com/SimonKrughoff/obs_file/tree/tickets/DM-6924)

# 0. Setup DM stack
```
source setupLSST-ghk1.sh
```

# 1. Get data

Here I use **filename=trial07.fits** as an example.

# 2. Get obs_file 

Assuming you have a DM stack set up.
You only need to do this `git clone` and `git checkout` once.
```
git clone https://github.com/SimonKrughoff/obs_file
cd obs_file
#git checkout tickets/DM-6924  ##temporally unavailable
git checkout 21fd0d51806c43bf335300a0bc97e409ed9c703e
```

Setup `obs_file`. You need to do this `setup` and `scons` everytime before you are going to use `obs_file`.
```
setup -k -r .
scons
cd ..
```

# 3. Setup repository 

For example, we call the working repo as 'repo' (or any name you like), you will need to run all the DMstack commands under this repo directory.

```
mkdir repo
cd repo
cp PATH_TO_YOUR_IMAGES . (cp /PATH/TO/trial07.fits . in this case)
```

* Make a directory to put things in
```
mkdir input
```

* Provide a mapper
```
echo "lsst.obs.file.FileMapper" > input/_mapper
```

# 4. Ingest the data
```
ingestImages.py input/ trial07.fits --mode link
```

# 5. Process the data
```
processCcd.py input/ --id filename=trial07.fits --config isr.noise=5 --output output
```
* Note that you need to make a pretty goood guess at the noise in the image.  This is something I'd like to fix.
