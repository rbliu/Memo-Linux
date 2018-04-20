
config.charImage.repair.cosmicray.nCrPixelMax=1000000

# Use psfex instead of pca
import lsst.meas.extensions.psfex.psfexPsfDeterminer
config.charImage.measurePsf.psfDeterminer.name='psfex'

config.isr.noise=0.03
config.isr.saturation=700

# size of cell used to determine PSF (pixels, column direction)
# config.charImage.measurePsf.psfDeterminer['psfex'].sizeCellX=1024
# config.charImage.measurePsf.psfDeterminer['psfex'].sizeCellY=1024

config.isr.isBackgroundSubtracted=True

# specify the minimum psfFlux for good Psf Candidates
config.charImage.measurePsf.starSelector['objectSize'].fluxMin=2500.0
config.charImage.measureApCorr.starSelector['objectSize'].fluxMin=2500
# config.charImage.measureApCorr.starSelector['objectSize'].fluxMax=300000
#
# specify the minimum psfFlux for good Psf Candidates
config.charImage.measurePsf.starSelector['secondMoment'].fluxLim=2500.0
config.charImage.measureApCorr.starSelector['secondMoment'].fluxLim=2500

# specify the minimum psfFlux for good Psf Candidates
# 	Valid Range = [0.0,inf)
config.charImage.measurePsf.starSelector['catalog'].fluxLim=2500.0
config.charImage.measureApCorr.starSelector['catalog'].fluxLim=2500.0
