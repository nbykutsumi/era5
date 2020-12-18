import myfunc.util as util
from datetime import datetime, timedelta
import os, sys
sys.path.append('/home/utsumi/anaconda2/envs/py27/lib/python2.7/site-packages')
import cdsapi
import netCDF4
import numpy as np
import socket

myhost=socket.gethostname()
if myhost =='shui':
    outbaseDir =  '/tank/utsumi/era5'
elif myhost=='well':
    outbaseDir = '/media/disk2/share/data/era5'
else:
    print 'check myhost',myhost
    sys.exit()

outDir = outbaseDir + '/orog'
util.mk_dir(outDir)
outPath= outDir + '/orog.geopotential.nc'

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',
        'format':'netcdf',
        'variable':'orography',
        'year':'2017',
        'month':'01',
        'day':'01',
        'time':'00:00'
    },
    outPath)

#-- Geopotential --> Geopotential Height ----
g = 9.80665  # m/s
with netCDF4.Dataset(outPath) as nc:
    gp = nc.variables['z'][0]  # m**2 / s**2

zmeter = (gp / g).data

zmeterPath = outDir + '/orog.meter.na.npy'
np.save(zmeterPath, zmeter)
print zmeterPath
