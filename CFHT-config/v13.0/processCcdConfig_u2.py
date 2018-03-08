# Apply the brighter fatter correction
config.isr.doBrighterFatter=False

config.charImage.repair.cosmicray.nCrPixelMax=1000000
#config.charImage.repair.cosmicray.nCrPixelMax=10000000

# Use psfex instead of pca
import lsst.meas.extensions.psfex.psfexPsfDeterminer
config.charImage.measurePsf.psfDeterminer.name='psfex'

# The following should be included for u filter in order to lower the source detection threshold
config.charImage.detection.includeThresholdMultiplier=1.0

# Run CModel
import lsst.meas.modelfit
config.charImage.measurement.plugins.names |= ["modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]

# The following is to use astrometry.net as the astrometry fitter / matcher
# Comment those lines if you want to use the defauft astrometry
#from lsst.meas.astrom.anetAstrometry import ANetAstrometryTask
#config.calibrate.astrometry.retarget(ANetAstrometryTask)
#config.calibrate.astrometry.solver.sipOrder=3

# Use new astrometry fitter
from lsst.meas.astrom import FitSipDistortionTask
config.calibrate.astrometry.wcsFitter.retarget(FitSipDistortionTask)

config.calibrate.astrometry.wcsFitter.order = 3
config.calibrate.astrometry.matcher.maxMatchDistArcSec=5

#config.charImage.astrometry.refObjLoader.filterMap = { 'i2': 'i'}

#Astrometry with sdss
config.calibrate.astromRefObjLoader.filterMap = {
	'u2': 'u',
}

# Photometry with sdss
config.calibrate.photoRefObjLoader.filterMap = {
	'u2': 'u',
}

import lsst.pipe.tasks.colorterms
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

# config.calibrate.doAstrometry = False
# config.calibrate.doPhotoCal = True
