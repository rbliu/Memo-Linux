# CFHT Reprocessing on `ghk1`

### Login to `ghk1`
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
`astrometry_net_data` has the corresponding astrometry reference files (`andConfig.py` and `*.fits`).


