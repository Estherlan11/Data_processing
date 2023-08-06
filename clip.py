#import the necessary packages
import rasterio
from rasterio.mask import mask
import geopandas as gpd

#input the Uganda boundary in vector format
inshp = '/home/s2283650/dissertation_data/boundary/gadm41_UGA_3.shp'
#input the clipped raster layer
inRas = '/home/s2283650/dissertation_data/UGA_300_M.tif'
#set the save path of result
outRas = '/home/s2283650/dissertation_data/all/'

#read the input file
Vector=gpd.read_file(inshp)

#loop all the features based on the field
for i in Vector['GID_3']:
    # Subsetting to temperary path
    Vector_tmp=Vector[Vector['GID_3']==i] 

    with rasterio.open(inRas) as src:
        Vector_tmp=Vector_tmp.to_crs(src.crs)
        out_image, out_transform=mask(src,Vector_tmp.geometry,crop=True)
        # copy the metadata of the source DEM
        out_meta=src.meta.copy() 
    
    out_meta.update({
        "driver":"Gtiff",
        "height":out_image.shape[1], # height starts with shape[1]
        "width":out_image.shape[2], # width starts with shape[2]
        "transform":out_transform
    })

    #save the result     
    with rasterio.open(outRas+'_'+str(i)+".tif",'w',**out_meta) as dst:
        dst.write(out_image)