# LSST DM Troubleshooting Logs

------
## For DM stack v17.0
------

* __Error__: In `processCcd`, FATAL error: `lsst::pex::exceptions::RuntimeError: 'DateTime not valid'`

  __Solution__: It's the new `astro_metadata_translator` issue in v17.0.1. New DECam header does NOT have `DTUTC` keyword since Nov 2017. A quick fix if to add the `DTUTC` keyword to the primary header of raw or instcal image (eg. DTUTC = 2018-12-12T07:14:51). You can use the `fitsAddDT.py` script in my [LSST_DM_Scripts](https://github.com/rbliu/LSST_DM_Scripts) github repository to do this.

------

* __Error__: In `processCcd`, FATAL error: `lsst::pex::exceptions::LengthError: 'Number of matches less than requested sip order'` or `RuntimeError: Unable to match sources`

  __Solution__: According to Dominique's comments, this is due to the high degree of SIP polynomial. You can try to limit it to 3rd or 2nd degree (in obs_cfht and obs_decam, the default is 4th):
  `config.calibrate.astrometry.wcsFitter.order = 2`

------

* __Error__: In `processCcd`, FATAL error: `lsst::pex::exceptions::RuntimeError: 'No valid points to fit. Variance is likely zero. Try weighting=False'`

  __Solution__: if this error happens to CCD2 in a __DECam__ image, it is normal. DECam CCD2 stopped working since Nov 2013. Just skip this CCD by specifying `--id visit=xxxxxxx ccdnum=1^3..60^62`

------
## For DM stack v13.0 and v14.0
------

* __Error__: with "exclusive lock" when using `eups`

  __Solution__: try adding this line
```
hooks.config.site.lockDirectoryBase = None
```
to the file `~/.eups/startup.py`.

------

* __Error__: some parameters in the config file are not recognized

  __Solution__: try commenting those lines.
------

* __Error__: asking you to add `--clobber-versions` or `--clobber-config`

  __Solution__: add it.
------

* __Error__: option `-C` has trouble locating the config file

  __Solution__: try the full option text `--configfile`.
------

* __Error__: `processCcd.py error: Unrecognized ID key 'ccdnum'`

  __Solution__: it means that wrong `--id` keys were used in `processCcd`. Make sure you are using `ccd` for CFHT data, and `ccdnum` for DECam data. For other telescopes, please read the whole error message.
------

* __Error__: `Could not find flux field(s): u2_camFLux, u2_flux.`

  __Solution__: It occurs in u2-filter images -- in the filter map of `obs_cfht`, the normal u-filter is mapping to `u.MP9301`, which you can find in their headers. But, some u images were using `u.MP9302`, which are ingested as "u2" by DMstack.

  Also be aware that this error is not only limited to u2 filter in CFHT data. If similar errors happen wot other data, try modifying the astrometry/photometry filter map part in the config file.
------

* __Error__: `Could not find matched sources` or `Unable to find andConfig.py in astrometry_net_data directory` or `no entries in posRefCat`

  __Solution__: You probably didn't setup astrometry correctly or your image cannot be covered by the astrometry you set up.

  Try to check the raw exposures to find out and through away the outliers. In the meantime, use `DM_14.0` with the new htm reference format.
