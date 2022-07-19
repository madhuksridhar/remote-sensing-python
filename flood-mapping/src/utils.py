

def create_clip(in_file, out_file, rowStart, rowEnd, colStart, colEnd):
    """
    """
    #Clip data to a rectangular boundary using GDAL
    from osgeo import gdal

    ## open
    src_ds = gdal.Open(in_file)

    ## clip rectangle width and height
    width =  9961  ## y coordinate
    height = 12601 ## x coordinate
    
    
    ## get the top left corner
    #geot = src_ds.GetGeoTransform()

    fileformat = "GTiff"
    driver = gdal.GetDriverByName(fileformat)

    dst_ds_clip = driver.Create(out_file, xsize = width, ysize = height, bands=1, eType = gdal.GDT_Float32)
    
    data = src_ds.GetRasterBand(1).ReadAsArray()

    dst_ds_clip.GetRasterBand(1).WriteArray(data[rowStart:rowEnd, colStart:colEnd])
    
    dst_ds_clip = None
    src_ds      = None 

