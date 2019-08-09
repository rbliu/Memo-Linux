import lsst.meas.modelfit
import lsst.shapelet

####################################
### This section is added to include shape measurements in the forced photometry catalog
### You can remove it if you don't need them.
import lsst.meas.extensions.shapeHSM
hsm_plugins = set([
    "ext_shapeHSM_HsmShapeBj",      # Bernstein & Jarvis 2002
	"ext_shapeHSM_HsmShapeLinear",  # Hirata & Seljak 2003
	"ext_shapeHSM_HsmShapeKsb",     # KSB 1995
	"ext_shapeHSM_HsmShapeRegauss", # Hirata & Seljak 2003
	"ext_shapeHSM_HsmSourceMoments",# Not PSF corrected; used by all of the above
	"ext_shapeHSM_HsmPsfMoments",   # Moments of the PSF, used by all of the above
])
config.measurement.plugins.names |= hsm_plugins

config.measurement.slots.shape = "ext_shapeHSM_HsmSourceMoments"
config.measurement.slots.psfShape = "ext_shapeHSM_HsmPsfMoments"
config.measurement.plugins["ext_shapeHSM_HsmShapeRegauss"].deblendNChild = "deblend_nChild"
####################################

config.measurement.plugins.names |= ["modelfit_GeneralShapeletPsfApprox", "modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]
config.measurement.slots.modelFlux = "modelfit_CModel"

config.doApCorr=True
