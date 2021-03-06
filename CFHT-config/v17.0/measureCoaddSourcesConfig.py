# Configuration file for measureCoaddSources

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

# We use CModel flux for color measurement (Bosch et al. 2017)
import lsst.meas.modelfit
import lsst.shapelet
#import lsst.meas.extensions.photometryKron
#    root.algorithms.names |= ["flux.kron"]
config.measurement.plugins.names |= ["modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]
config.measurement.slots.modelFlux = "modelfit_CModel"

config.doApCorr=True


# No u band in PS1
config.match.refObjLoader.ref_dataset_name='pan-starrs'
config.match.refObjLoader.filterMap={
    'g':'g',
    'r':'r',
    'i':'i',
    'z':'z',
}

# Maximum linear dimension for footprints before they are ignored as large; non-positive means no threshold applied
#config.deblend.maxFootprintSize=2000  # same as for processCcd
