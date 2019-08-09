from lsst.obs.decam.decamNullIsr import DecamNullIsrTask
config.isr.retarget(DecamNullIsrTask)

# Use PSFEx instead of PCA
import lsst.meas.extensions.psfex.psfexPsfDeterminer
config.charImage.measurePsf.psfDeterminer.name='psfex'

# use CModel flux for color measurement (Bosch et al. 2017)
import lsst.meas.modelfit
config.charImage.measurement.plugins.names |= ["modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]
config.charImage.measurement.slots.modelFlux = "modelfit_CModel"

# Set SIP order to 3 (default is 5), the Task default before RFC-577 to maintain same behavior
config.calibrate.astrometry.wcsFitter.order = 3

#from lsst.meas.algorithms import LoadIndexedReferenceObjectsTask
#config.calibrate.astromRefObjLoader.retarget(LoadIndexedReferenceObjectsTask)
#config.calibrate.photoRefObjLoader.retarget(LoadIndexedReferenceObjectsTask)

#config.calibrate.astromRefObjLoader.ref_dataset_name='pan-starrs'
#config.calibrate.photoRefObjLoader.ref_dataset_name='pan-starrs'

# color terms
config.calibrate.photoCal.photoCatName = "pan-starrs"
config.calibrate.photoCal.applyColorTerms = True
import lsst.pipe.tasks.colorterms
colorterms = config.calibrate.photoCal.colorterms
from lsst.pipe.tasks.colorterms import ColortermDict, Colorterm
colorterms.data["pan-starrs"] = ColortermDict(data={
	    'g': Colorterm(primary="g", secondary="i", c0=0.00062, c1=0.03604, c2=0.01028),
		'r': Colorterm(primary="g", secondary="i", c0=0.00495, c1=-0.08435, c2=0.03222),
		'i': Colorterm(primary="g", secondary="i", c0=0.00904, c1=-0.04171, c2=0.00566),
		'z': Colorterm(primary="g", secondary="i", c0=0.02583, c1=-0.07690, c2=0.02824),
		'Y': Colorterm(primary="g", secondary="i", c0=0.02332, c1=-0.05992, c2=0.02840)
})
