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
    outbaseDir = '/media/disk2/data/era5'
else:
    print('check myhost',myhost)
    sys.exit()

grid = [0.5625,0.5625]
if grid is None:
    sgrid='org'
elif grid == [0.5625,0.5625]:
    sgrid='deg05625'
else:
    print('check grid',grid)
    sys.exit()

outDir = outbaseDir + '/%s/fix'%(sgrid)
util.mk_dir(outDir)
outPath= outDir + '/lsm.nc'

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',
        'format':'netcdf',
        'variable':'land_sea_mask',
        'year':'2017',
        'month':'01',
        'day':'01',
        'time':'00:00',
        'grid'  : grid,     # Latitude/longitude grid.           Default: 0.25 x 0.257
    },
    outPath)
print(outPath)
