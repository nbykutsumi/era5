import cdsapi
import myfunc.util as util
from datetime import datetime, timedelta
import socket

myhost=socket.gethostname()
if myhost =='shui':
    outbaseDir =  '/tank/utsumi/era5'
elif myhost=='well':
    outbaseDir = '/media/disk2/share/data/era5'
else:
    print 'check myhost',myhost
    sys.exit()


iDTime = datetime(2017,6,1)
eDTime = datetime(2017,6,30)
dDTime = timedelta(days=1)
lDTime = util.ret_lDTime(iDTime,eDTime,dDTime)[::-1]
#lvar = ['temperature']
#lvar = ['relative_humidity']
#lvar = ['geopotential','specific_humidity','temperature']
lvar = ['geopotential','specific_humidity','temperature','vertical_velocity','vorticity','relative_humidity']
llev = ['200','300','450','600','750','825','900','975']

c = cdsapi.Client()
dvarName = {'geopotential':'z','relative_humidity':'r','specific_humidity':'q','temperature':'t'
            ,'vertical_velocity':'w', 'vorticity':'vo'}


for DTime in lDTime:
    Year,Mon,Day = DTime.timetuple()[:3]

    #if Day==3: continue  # test

    for var in lvar:
        varName= dvarName[var]
        outDir = outbaseDir + '/%s/%04d%02d'%(varName,Year,Mon)

        util.mk_dir(outDir)
        outPath= outDir + '/%s.%04d.%02d.%02d.nc'%(varName,Year,Mon,Day)

        c.retrieve(
            'reanalysis-era5-pressure-levels',
            {
                'product_type':'reanalysis',
                'variable':[var],
                'pressure_level':llev,
                'year':'%04d'%(Year),
                'month':'%02d'%(Mon),
                'day':'%02d'%(Day),
                'time':[
                    '00:00','01:00','02:00',
                    '03:00','04:00','05:00',
                    '06:00','07:00','08:00',
                    '09:00','10:00','11:00',
                    '12:00','13:00','14:00',
                    '15:00','16:00','17:00',
                    '18:00','19:00','20:00',
                    '21:00','22:00','23:00'
                ],
                'format':'netcdf'
            },
            outPath)




