import os.path
from lsst.utils import getPackageDir

decamConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')
config.isr.load(os.path.join(decamConfigDir, 'isr.py'))

# Use psfex instead of pca
import lsst.meas.extensions.psfex.psfexPsfDeterminer
config.charImage.measurePsf.psfDeterminer.name='psfex'

# Run CModel
import lsst.meas.modelfit
import lsst.meas.extensions.convolved  # noqa: Load flux.convolved algorithm
config.charImage.measurement.plugins.names |= ["modelfit_DoubleShapeletPsfApprox",
                                               "modelfit_CModel"]
config.charImage.measurement.slots.modelFlux = "modelfit_CModel"

# Run astrometry using the new htm reference catalog format
# The following retargets are necessary until the new scheme becomes standard
#from lsst.meas.algorithms import LoadIndexedReferenceObjectsTask
#config.charImage.refObjLoader.retarget(LoadIndexedReferenceObjectsTask)
#config.calibrate.astromRefObjLoader.retarget(LoadIndexedReferenceObjectsTask)
#config.calibrate.photoRefObjLoader.retarget(LoadIndexedReferenceObjectsTask)

# Use new astrometry fitter
#from lsst.meas.astrom import FitSipDistortionTask
#config.calibrate.astrometry.wcsFitter.retarget(FitSipDistortionTask)

config.calibrate.astrometry.wcsFitter.order = 3
#config.calibrate.astrometry.matcher.maxMatchDistArcSec=5

# Select external catalogs for Astrometry and Photometry
#config.charImage.refObjLoader.ref_dataset_name = 'pan-starrs'
#config.charImage.refObjLoader.ref_dataset_name = 'sdss'
#config.calibrate.photoRefObjLoader.ref_dataset_name='pan-starrs'
#config.calibrate.photoRefObjLoader.ref_dataset_name='sdss'
#config.calibrate.astromRefObjLoader.ref_dataset_name='gaia'
#config.calibrate.astromRefObjLoader.ref_dataset_name='pan-starrs'
#config.calibrate.astromRefObjLoader.ref_dataset_name='sdss'

# Astrometry with panstarrs
#config.calibrate.astromRefObjLoader.filterMap = {
#     'u':'g',
#     'Y':'y',
#}

# Photometry with panstarrs
#config.calibrate.photoRefObjLoader.filterMap = {
#	  'u':'g',
#	  'Y':'y',
#}

# Astrometry with gaia
#config.calibrate.astromRefObjLoader.filterMap = {
#    'u':'phot_g_mean_mag',
#    'g':'phot_g_mean_mag',
#    'r':'phot_g_mean_mag',
#    'i':'phot_g_mean_mag',
#    'z':'phot_g_mean_mag',
#    'Y':'phot_g_mean_mag',
#}

# Photometry with sdss
#config.calibrate.photoRefObjLoader.filterMap = {
#	 'u': 'U',
#	 'g': 'G',
#	 'r': 'R',
#	 'i': 'I',
#	 'z': 'Z',
#	 'y': 'Z',
#}

#Astrometry with sdss
#config.calibrate.astromRefObjLoader.filterMap = {
#	 'u': 'U',
#	 'g': 'G',
#	 'r': 'R',
#	 'i': 'I',
#	 'z': 'Z',
#	 'y': 'Z',
#}

import lsst.pipe.tasks.colorterms
config.calibrate.photoCal.photoCatName = "pan-starrs"
config.calibrate.photoCal.applyColorTerms = True
colorterms = config.calibrate.photoCal.colorterms
from lsst.pipe.tasks.colorterms import ColortermDict, Colorterm
colorterms.data["pan-starrs"] = ColortermDict(data={
	    'g': Colorterm(primary="g", secondary="i", c0=0.00062, c1=0.03604, c2=0.01028),
		'r': Colorterm(primary="g", secondary="i", c0=0.00495, c1=-0.08435, c2=0.03222),
		'i': Colorterm(primary="g", secondary="i", c0=0.00904, c1=-0.04171, c2=0.00566),
		'z': Colorterm(primary="g", secondary="i", c0=0.02583, c1=-0.07690, c2=0.02824),
		'Y': Colorterm(primary="g", secondary="i", c0=0.02332, c1=-0.05992, c2=0.02840)
})
