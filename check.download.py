import glob
import subprocess

scmd = 'ls /media/disk2/data/era5/deg05625/*'
subprocess.call(scmd, shell=True)

