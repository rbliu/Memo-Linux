# Trouble-shooting


* __Error__ with "exclusive lock" when using `eups` 

  __Solution__: try adding this line
```
hooks.config.site.lockDirectoryBase = None
```
to the file `~/.eups/startup.py`.

------

* __Error__: some parameters in the config file are not recognized

  __Solution__: try commending those lines.
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
