#import the necessary packages
import os
import glob
import arcpy
from arcpy.sa import *

'''
Function:
    Calculate the average of all raster data in the input folder inws
'''

#check the permission
arcpy.CheckOutExtension("ImageAnalyst") 
arcpy.CheckOutExtension("spatial")

# Input the file paths 
inpath = r'E:\newdata\hos'

OutputFile = open(inpath + 'mean.csv', 'w')

# Use the glob package to read and store all tif files under inws into rasters
rasters = glob.glob(os.path.join(inpath, "*.tif"))
whereClause = "VALUE = 0"   # remove outliers

# Loop over all the images in rasters and "average" them.
for ras in rasters:
    arcpy.CalculateStatistics_management(ras)
    meanValueInfo = arcpy.GetRasterProperties_management(ras, 'MEAN')
    meanValue = meanValueInfo.getOutput(0)
    print(os.path.basename(ras) + ',' + str(meanValue) + '\n')
    OutputFile.write(os.path.basename(ras) + ',' + str(meanValue) + '\n')

OutputFile.close()
print("All project is OK!")
