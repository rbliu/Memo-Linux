# Trouble-shooting


* If you got error with "exclusive lock" when using `eups`, try adding this line
```
hooks.config.site.lockDirectoryBase = None
```
to the file `~/.eups/startup.py`.

------

* If some parameters in the config file are not recognized, try commending those lines.
------

* If the error asks you to add `--clobber-version` or `--clobber-config`, add it.
------

* If option `-C` has trouble locating the config file, try the full option text `--configfile`.
------

* `processCcd.py error: Unrecognized ID key 'ccdnum'` means that wrong `--id` keys were used in `processCcd`. Make sure you are using `ccd` for CFHT data, and `ccdnum` for DECam data. For other telescopes, please read the whole error message.
