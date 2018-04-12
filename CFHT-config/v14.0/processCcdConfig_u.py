# Apply the brighter fatter correction
config.isr.doBrighterFatter=False

config.charImage.repair.cosmicray.nCrPixelMax=1000000

# Useul to get to avoid deblending of satellite tracks
config.calibrate.deblend.maxFootprintSize=2000 # 2200

# Use psfex instead of pca
import lsst.meas.extensions.psfex.psfexPsfDeterminer
config.charImage.measurePsf.psfDeterminer.name='psfex'

# The following should be included for u filter in order to lower the source detection threshold
config.charImage.detection.includeThresholdMultiplier=1.0

# Run CModel
import lsst.meas.modelfit
config.charImage.measurement.plugins.names |= ["modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]

# Run astrometry using the new htm reference catalog format
# The following retargets are necessary until the new scheme becomes standard
from lsst.meas.algorithms import LoadIndexedReferenceObjectsTask
config.charImage.refObjLoader.retarget(LoadIndexedReferenceObjectsTask)
config.calibrate.astromRefObjLoader.retarget(LoadIndexedReferenceObjectsTask)
config.calibrate.photoRefObjLoader.retarget(LoadIndexedReferenceObjectsTask)

# Use new astrometry fitter
from lsst.meas.astrom import FitSipDistortionTask
config.calibrate.astrometry.wcsFitter.retarget(FitSipDistortionTask)

config.calibrate.astrometry.wcsFitter.order = 3
config.calibrate.astrometry.matcher.maxMatchDistArcSec=5

# Select external catalogs for Astrometry and Photometry
#config.charImage.refObjLoader.ref_dataset_name = 'pan-starrs'
config.charImage.refObjLoader.ref_dataset_name = 'sdss'
config.calibrate.photoRefObjLoader.ref_dataset_name='sdss'
#config.calibrate.astromRefObjLoader.ref_dataset_name='gaia'
config.calibrate.astromRefObjLoader.ref_dataset_name='sdss'
#config.calibrate.astromRefObjLoader.ref_dataset_name='sdss'

# Astrometry with panstarrs
# config.calibrate.astromRefObjLoader.filterMap = {
#     'u':'g',
#     'g':'g',
#     'r':'r',
#     'i':'i',
#     'i2':'i',
#     'z':'z',
#     'y':'y',
# }
# Astrometry with gaia
#config.calibrate.astromRefObjLoader.filterMap = {
#    'u':'phot_g_mean_mag',
#    'g':'phot_g_mean_mag',
#    'r':'phot_g_mean_mag',
#    'i':'phot_g_mean_mag',
#    'z':'phot_g_mean_mag',
#    'y':'phot_g_mean_mag',
#}
# Photometry with sdss
config.calibrate.photoRefObjLoader.filterMap = {
    'u': 'U',
    'u2': 'U',
    'g': 'G',
    'r': 'R',
    'i': 'I',
    'i2': 'I',
    'z': 'Z',
    'y': 'Z',
}

#Astrometry with sdss
config.calibrate.astromRefObjLoader.filterMap = {
    'u': 'U',
    'u2': 'U',
    'g': 'G',
    'r': 'R',
    'i': 'I',
    'z': 'Z',
    'y': 'Z',
}

import lsst.pipe.tasks.colorterms
config.calibrate.photoCal.colorterms.data['e2v'].data['i2']=lsst.pipe.tasks.colorterms.Colorterm()
config.calibrate.photoCal.colorterms.data['e2v'].data['i2'].c2=0.0
config.calibrate.photoCal.colorterms.data['e2v'].data['i2'].c1=0.003
config.calibrate.photoCal.colorterms.data['e2v'].data['i2'].c0=0.0
config.calibrate.photoCal.colorterms.data['e2v'].data['i2'].primary='i'
config.calibrate.photoCal.colorterms.data['e2v'].data['i2'].secondary='r'

config.calibrate.photoCal.colorterms.data['e2v'].data['u2']=lsst.pipe.tasks.colorterms.Colorterm()
config.calibrate.photoCal.colorterms.data['e2v'].data['u2'].c2=0.0
config.calibrate.photoCal.colorterms.data['e2v'].data['u2'].c1=0.241
config.calibrate.photoCal.colorterms.data['e2v'].data['u2'].c0=0.0
config.calibrate.photoCal.colorterms.data['e2v'].data['u2'].primary='u'
config.calibrate.photoCal.colorterms.data['e2v'].data['u2'].secondary='g'

# use Chebyshev background estimation
config.charImage.background.useApprox=True
config.charImage.detection.background.binSize=128
config.charImage.detection.background.useApprox=True
config.charImage.background.binSize = 128
config.charImage.background.undersampleStyle = 'REDUCE_INTERP_ORDER'
config.charImage.detection.background.binSize = 128
config.charImage.detection.background.undersampleStyle='REDUCE_INTERP_ORDER'
config.charImage.detection.background.binSize = 128
config.charImage.detection.background.undersampleStyle = 'REDUCE_INTERP_ORDER'
