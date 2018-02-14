# CFHT Reprocessing on `ghk1`


## 1. Login to `ghk1`

ssh to `ghk1` and setup DMstack. On `ghk1`, we have a `v13.0` version of DMstack installed. 

**Sample config files can be found at https://github.com/LSSTDESC/ReprocessingTaskForce/tree/master/config**

```
ssh ghk1
bash

cd /export/rliu/lsstsw
. bin/setup.sh
setup lsst_distrib
```
If you have permission issue, send me an email (byliu1990(at)gmail.com)

We take *A85* CFHT data as an example:
```
working directory
.
|-- A85_good_g.list
|-- A85_good_r.list
|-- A85_good_u.list
|
|-- astrometry_net_data/
|   |-- andConfig.py
|   |-- sdss-dr9-fink-v5b_and_282_0.fits
|   |-- sdss-dr9-fink-v5b_and_282_1.fits
|   `-- sdss-dr9-fink-v5b_and_282_2.fits
|-- config/
|
|-- input/
|   |-- _mapper
|   |-- raw
|   |   `-- 04BF02
|   |       `-- Abell\ 85
|   |           |-- 2004-08-21
|   |           |   `-- u
|   |           |       |-- 758880p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/758880p.fits.fz
|   |           |       |-- 758881p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/758881p.fits.fz
|   |           |       `-- 758882p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/758882p.fits.fz
|   |           `-- 2004-09-17
|   |               |-- g
|   |               |   |-- 762104p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/762104p.fits.fz
|   |               |   |-- 762105p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/762105p.fits.fz
|   |               |   `-- 762106p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/762106p.fits.fz
|   |               `-- r
|   |                   |-- 762114p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/762114p.fits.fz
|   |                   |-- 762115p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/762115p.fits.fz
|   |                   `-- 762116p.fits.fz -> /net/mangrove/export/data/astro/rliu/cfht/A85/rawData/762116p.fits.fz
|   `-- registry.sqlite3
|
`-- rawData/
    |-- 758880p.fits.fz
    |-- 758881p.fits.fz
    |-- 758882p.fits.fz
    |-- 762104p.fits.fz
    |-- 762105p.fits.fz
    |-- 762106p.fits.fz
    |-- 762114p.fits.fz
    |-- 762115p.fits.fz
    `-- 762116p.fits.fz

```
where `rawData` has all the CFHT-processed images (`.fits` or `.fits.fz`);

`astrometry_net_data` has the corresponding astrometry reference files (`andConfig.py` and `*.fits`);

`config` has all the config files.


## 2. Setup astrometry reference

Follow [these steps](https://github.com/rbliu/Memo-Linux/blob/master/Getting_astrometry_files.md) to create the astrometry repo for this cluster.

(The `astrometry_net_data` directory can be anywhere. I created it under the same working directory for convenience.)

To setup astreometry reference:
```
cd astrometry_net_data
eups declare -m none -r . astrometry_net_data -t $USER && setup astrometry_net_data -t $USER
cd ..
```


## 3. ingestImages

First, we need to ingest the data:
```
ingestImages.py input rawData/*.fz --mode link
```

where `input` gives the sub-directory to save the ingested data,

and `--mode link` will create links instead of copying files


## 4. processCcd

For CFHT data, the file names are their "visit" or "exposure" ids. So we can process single CCD using:
```
processCcd.py input --output output --id visit=758880 ccd=10 -C config/processCcdConfig.py
```

Or process all CCDs in one exposure:
```
processCcd.py input --output output --id visit=758880 -C config/processCcdConfig.py
```

Or process all exposures for one filter:
```
processCcd.py input --output output @A85_good_g.list -C config/processCcdConfig.py -j 4
```
where `A85_good_g.list` has
```
--id visit=762104
--id visit=762105
--id visit=762106
```

and `-j 4` means using 4 cores (or threads) for parallel -- modify this number according to your machine.

**Note: if there is no `output` directory before running `processCcd.py`, it will be created; if there is already an `output` directory with previous processed data, `processCcd.py` will overwrite output into it.**



## 5. coadd

### 5.1 Create a skymap

To determine the skymap coordinates

```
makeDiscreteSkyMap.py output --output output/coadd_dir @A85_good_g.list -C config/makeDiscreteSkyMapConfig.py
```

and its output should look like:
```
makeDiscreteSkyMap INFO: tract 0 has corners (11.738, -10.594), (9.064, -10.594), (9.074, -7.965), (11.728, -7.965) (RA, Dec deg) and 9 x 9 patches
```

### 5.2 Identify the list of (tract,patch)

From the output of the previous step, get the coordinates of the lower left and upper right corners in order to pass them to the following command:

```
reportPatches.py output/coadd_dir --config raDecRange="9.074, -10.594, 11.728, -7.965" --id tract=0 patch=0,0 filter=g > patches.txt
```

where `--id tract=0 patch=0,0` is meaningless but mandatory.

Then we need to modify a little bit the `patches.txt` file:
```
sed -e 's/^/--id filter=g /' patches.txt > patches_g.txt
```

LSST processed data have the (tract,patch) layout. Usually, for one exposure, we have its `tract=0` and `patch=0,0` to `9,9`.


### 5.3 Warp images to adjust them to the sky map patches

Create a file `A85_coadd_good_g.list` containing the following:
```
--selectId filter=g visit=762104
--selectId filter=g visit=762105
--selectId filter=g visit=762106
```

and run：
```
makeCoaddTempExp.py output --output output/coadd_dir --id filter=g @patches_g.txt @A85_coadd_good_g.list -C config/makeCoaddTempExpConfig.py -j 4
```

This will create one warped image for each visit/CCD contributing to a each given patch/tract.

It is safe to append `--timeout 9999999` option to avoid timeout error.

Now, there should be warped pieces of images under
```
./output/coadd_dir/deepCoadd/g/0/0,0tempExp/ ~ 9,9tempExp/
```


### 5.4 Assemble the coadded images

Assemble the temp exposures for each patch:
```
assembleCoadd.py output --output output/coadd_dir @patches_g.txt @A85_coadd_good_g.list -C config/assembleCoaddConfig.py
```





------
### Trouble-shooting


* If you got error with "exclusive lock" when using `eups`, try adding this line
```
hooks.config.site.lockDirectoryBase = None
```
to the file `~/.eups/startup.py`.


* If some parameters in the config file are not recognized, try commending those lines.


* If option `-C` has trouble locating the config file, try the full text `--configfile`.
