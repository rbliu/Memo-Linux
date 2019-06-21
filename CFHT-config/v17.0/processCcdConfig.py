# Astrometry dataset on mangrove is named as 'pan-starrs'
for refObjLoader in (config.calibrate.astromRefObjLoader,
                     config.calibrate.photoRefObjLoader,
                     config.charImage.refObjLoader,
                     ):
    refObjLoader.filterMap = {'i2': 'i'}
    refObjLoader.ref_dataset_name = "pan-starrs"
