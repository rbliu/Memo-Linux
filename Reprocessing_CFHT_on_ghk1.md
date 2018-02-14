# CFHT Reprocessing on `ghk1`


### Login to `ghk1`

ssh to `ghk1` and setup DMstack. On `ghk1`, we have a `v13.0` version of DMstack installed.

```
ssh ghk1
bash

cd /export/rliu/lsstsw
. bin/setup.sh
setup lsst_distrib
```
If you have permission issue, send me an email (byliu1990(at)gmail.com)

We take A85 CFHT data as an example:
```
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


### Setup astrometry reference

Follow the steps in https://github.com/rbliu/Memo-Linux/blob/master/Getting_astrometry_files.md

(The `astrometry_net_data` directory can be anywhere. I created it under the same working directory for convenience.)

To setup astreometry reference:
```
cd astrometry_net_data
eups declare -m none -r . astrometry_net_data -t $USER && setup astrometry_net_data -t $USER
cd ..
```


### ingestImages

First, we need to ingest the data:
```
ingestImages.py input rawData --mode link
```

`--mode link` will create links instead of copying files


### processCcd

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
processCcd.py input --output output @A85_good_g.list -C config/processCcdConfig_old.py
```
where `A85_good_g.list` has
```
--id visit=762104
--id visit=762105
--id visit=762106
```





------
### Trouble-shooting

* If you got error with "exclusive lock" when using `eups`, try adding this line
```
hooks.config.site.lockDirectoryBase = None
```
to the file `~/.eups/startup.py`.
