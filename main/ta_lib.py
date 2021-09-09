import numpy
import talib

# https://mrjbq7.github.io/ta-lib/install.html
# install on Mac, windows, then install with pip
close = numpy.random.random(100)

#Calculate a simple moving average of the close prices:
output = talib.SMA(close)
#%%



