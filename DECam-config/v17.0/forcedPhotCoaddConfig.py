import lsst.meas.modelfit
import lsst.shapelet

config.measurement.plugins.names |= ["modelfit_GeneralShapeletPsfApprox", "modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]
config.measurement.slots.modelFlux = "modelfit_CModel"

config.doApCorr=True
