import rasterio
from rasterio.mask import mask
import geopandas as gpd

inshp = '/home/ec2-user/data/hybas_sa_lev01-12_v1c/hybas_sa_lev06_v1c.shp'
inRas = '/home/ec2-user/data/SmallDEM_Testing.tif'
outRas = '/home/ec2-user/data/ClippedSmallRaster.tif'


Vector=gpd.read_file(inshp)

Vector=Vector[Vector['HYBAS_ID']==6060122060] # Subsetting to my AOI

with rasterio.open(inRas) as src:
    Vector=Vector.to_crs(src.crs)
    # print(Vector.crs)
    out_image, out_transform=mask(src,Vector.geometry,crop=True)
    out_meta=src.meta.copy() # copy the metadata of the source DEM
    
out_meta.update({
    "driver":"Gtiff",
    "height":out_image.shape[1], # height starts with shape[1]
    "width":out_image.shape[2], # width starts with shape[2]
    "transform":out_transform
})
              
with rasterio.open(outRas,'w',**out_meta) as dst:
    dst.write(out_image)