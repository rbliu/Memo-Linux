import lsst.meas.modelfit
import lsst.shapelet

config.measurement.plugins.names |= ["modelfit_GeneralShapeletPsfApprox", "modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]
config.measurement.slots.modelFlux = "modelfit_CModel"

config.doApCorr=True

config.measurement.plugins['base_PixelFlags'].masksFpAnywhere.append('CLIPPED')

# extendedness = mag_PSF - mag_CModel
# ~ 0: star; > 0: galaxy
config.catalogCalculation.plugins.names = ["base_ClassificationExtendedness"]
config.measurement.slots.psfFlux = "base_PsfFlux"
