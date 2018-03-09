# use "instcal" exposures from the community pipeline until DecamIsrTask is up to snuff
from lsst.obs.decam.decamNullIsr import DecamNullIsrTask
config.isr.retarget(DecamNullIsrTask)

# Shape measurements with HSM-regauss
import os.path
from lsst.utils import getPackageDir
config.calibrate.measurement.load(os.path.join(getPackageDir("meas_extensions_shapeHSM"), "config", "enable.py"))
config.calibrate.measurement.plugins["ext_shapeHSM_HsmShapeRegauss"].deblendNChild = "deblend_nChild"

config.calibrate.doAstrometry = False
config.calibrate.doPhotoCal = False
