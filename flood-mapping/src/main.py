from utils import *


# filename 
archive_img = "S1A_IW_GRDH_1SSV_20150320T114745_20150320T114810_005115_0066FA_82D7.SAFE/measurement/s1a-iw-grd-vv-20150320t114745-20150320t114810-005115-0066fa-001.tiff"
archive_img_clip = "s1a-iw-grd-vv-20150320t114745_clip.tiff"

crisis_img = "S1A_IW_GRDH_1SSV_20150904T114747_20150904T114812_007565_00A772_B9FD.SAFE/measurement/s1a-iw-grd-vv-20150904t114747-20150904t114812-007565-00a772-001.tiff "
crisis_img_clip = "s1a-iw-grd-vv-20150904t114747_clip.tiff"

# Step 1: Clip data to a rectangular boundary using GDAL
rowStart = 3903
rowEnd =  16503
    
colStart = 13058
colEnd =  12018

create_clip(archive_img, archive_img_clip, rowStart, rowEnd, colStart, colEnd)
#create_clip(crisis_img, crisis_img_clip, rowStart, rowEnd, colStart, colEnd)

