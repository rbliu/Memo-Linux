__$$$$$ Redundant file $$$$$__

_This instruction is based on the [Wiki page of CFHTLS-reprocessing](https://github.com/LSSTDESC/ReprocessingTaskForce/wiki) and [another obs_decam tutorial documentation](https://www.overleaf.com/read/vmnstztyfbht). In addition to giving credit to the editors of the Wiki page, I also greatly appreciate help from Dominique Boutigny, Shenming Fu, Jim Bosch, Dominique Fouchez, Robert Lupton, Simon Krughoff, Nicolas Chotard, Johann Cohen-Tanugi, Meredith Rawls, Kian-Tat Lim, Colin Slater, Chris Waters, John Parejko, and all the experts in DM team and the LSST Community. This instruction is only used as personal technical notes which belongs to Ian Dell'Antonio's group, and by no means to be published. Any code in this instruction is open-source and without any warranty._

# (In construction) DECam Reprocessing on `ghk1`


## 1. Login to `ghk1`

ssh to `ghk1` and setup DMstack. We have a `v17.0` version of DMstack installed.

**Sample config files can be found at https://github.com/LSSTDESC/ReprocessingTaskForce/tree/master/config**

```
ssh ghk1
bash
source /net/mangrove/export/data/astro/lsst_stack_v17_0_1/loadLSST.bash
setup lsst_distrib
```
If you have permission issue, send me an email (byliu1990(at)gmail.com)

You can process either DECam Community Pipeline products (instrumental calibrated images) or raw data. As for now, the masks in the CP products may cause some issue in `processCcd`. So we suggest using raw data.

Suppose the working directory is named as `DECam_repo`. In this directory, create some sub-directories:
```
mkdir raw_data config MasterCal_bias MasterCal_flat
mkdir -p DATA/CALIB/2013-01-01
```

where `DATA` is the main directory for processing data;

`raw_data` has all the raw DECam images (`.fits.fz`);

`config` is where you store all the config files.


## 2. Setup astrometry reference

We have Gaia/Pan-STARRS-1/SDSS reference catalogs for astrometry and photometry calibration. By default, PS1 is used as both astrometry and photometry calibration. You can also choose Gaia catalog for astrometry.

To setup astrometry reference:
```
ca DATA
ln -s /export/rliu/refcats/htm_baseline ref_cats
```


## 3. Ingest Images and Master Calibration files

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

**Note: If there is no `output` directory before running `processCcd.py`, it will be created; if there is already an `output` directory with previous processed data, `processCcd.py` will overwrite output into it.**

The output repository usually contains:
```
calexp	config	icSrc  metadata  repositoryCfg.yaml  schema  src  srcMatch
```

where `calexp` and `src` are two important outputs.

`calexp` are calibrated exposures (Multi-Extension FITS) with these extensions:
* image
* mask
* variance

`src` are source catalogs (FITS table), which include all measurements.

**Note: These images and measurements are just preliminary results from `processCcd.py`. To obtain advanced results, you need to go through the following steps until forced photometry.**



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

The assebled images are:
```
./output/coadd_dir/deepCoadd/g/0/0,0.fits ~ 9,9.fits
```



## 6. Multi-band processing

Repeat the coadd steps for each filter. And go through the multi-band processing steps for one patch (*Don't forget to add the [corresponding config files](https://github.com/LSSTDESC/ReprocessingTaskForce/tree/master/config)*):
```
detectCoaddSources.py output/coadd_dir --output output/coadd_dir --id filter=g tract=0 patch=5,3
mergeCoaddDetections.py output/coadd_dir --output output/coadd_dir --id tract=0 patch=5,3 filter=g^r^i
measureCoaddSources.py output/coadd_dir --output output/coadd_dir --id tract=0 patch=5,3 filter=g
mergeCoaddMeasurements.py output/coadd_dir --output output/coadd_dir --id tract=0 patch=5,3 filter=g^r^i
```

Or run it for the whole tract:
```
detectCoaddSources.py output/coadd_dir --output output/coadd_dir --id filter=g tract=0
mergeCoaddDetections.py output/coadd_dir --output output/coadd_dir --id tract=0 filter=g^r^i
measureCoaddSources.py output/coadd_dir --output output/coadd_dir --id tract=0 filter=g
mergeCoaddMeasurements.py output/coadd_dir --output output/coadd_dir --id tract=0 filter=g^r^i
```

Or save the `--id` option as a `.list`/`.txt` file, and run the command with `@patch_g.txt`.

Each coadd source is detected / deblended / measured using `CModel` -- make sure you have it in the config file:
```
import lsst.meas.modelfit
import lsst.shapelet
config.measurement.plugins.names |= ["modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]
config.measurement.slots.modelFlux = "modelfit_CModel"
```

The multiband processing guarantees that if 1 source is identified and measured in 1 band, there is also corresponding sources in the other bands.

`CModel` fits an exponential and a de Vaucouleur separately, then fit a linear combination of the two while holding the ellipse parameters fixed at the best fit values from an independent fitting.


## 7. Forced photometry

In forced photometry the source detection and galaxy shape measurement is performed in a reference band and the photometry is measured in the other bands assuming that the same galaxy shape (even if it is not detected).

It can be run at the CCD level (`forcedPhotCcd.py`) or at the coadd level (`forcedPhotCoadd.py`).

To run forced photometry on one patch:
```
forcedPhotCoadd.py output/coadd_dir --output output/coadd_dir --id tract=0 patch=5,3 filter=g -C config/forcedPhotCoaddConfig.py
```
