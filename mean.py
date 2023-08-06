import os
import glob
import arcpy
from arcpy.sa import *

'''
功能：
    计算输入文件夹inws内，所有栅格数据的平均值
'''

arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.CheckOutExtension("spatial")

# 输入路径  应该注意，中文路径，会导致读不出文件；路径尽量不要有空格，写文件时会报错
inpath = r'E:\newdata\hos'

OutputFile = open(inpath + 'mean.csv', 'w')

# 利用glob包，将inws下的所有tif文件读存放到rasters中
rasters = glob.glob(os.path.join(inpath, "*.tif"))
whereClause = "VALUE = 0"  # 去除异常值

# 循环rasters中的所有影像，进行“求平均值”操作
for ras in rasters:
    arcpy.CalculateStatistics_management(ras)
    meanValueInfo = arcpy.GetRasterProperties_management(ras, 'MEAN')
    meanValue = meanValueInfo.getOutput(0)
    print(os.path.basename(ras) + ',' + str(meanValue) + '\n')
    OutputFile.write(os.path.basename(ras) + ',' + str(meanValue) + '\n')

OutputFile.close()
print("All project is OK！")

