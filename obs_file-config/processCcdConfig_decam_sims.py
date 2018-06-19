# Use psfex instead of pca
import lsst.meas.extensions.psfex.psfexPsfDeterminer
config.charImage.measurePsf.psfDeterminer.name='psfex'

config.charImage.repair.cosmicray.nCrPixelMax=100000

config.isr.noise=0.1                                                                                          

config.isr.isBackgroundSubtracted=True
