"""
Created on Thu May  6 17:54:34 2021

@author: mathew

"""

import geemap
import ee
from eeauth import eeauth
from ee_functions import draw_region_rect,gsw_reclass,awc_reclass,make_potinfil


p_key = "/home/mathew/hdd/UBU20/hdd/TCR/GIT/StopRunoff/assets/geengine-312606-81c6465d7301.json"
service_account = 'geengine@geengine-312606.iam.gserviceaccount.com '
lat = 36.9
lon = 50.01

layers = ['USGS/SRTMGL1_003','JRC/GSW1_0/GlobalSurfaceWater'
          ,"OpenLandMap/SOL/SOL_TEXTURE-CLASS_USDA-TT_M/v02",
          "OpenLandMap/SOL/SOL_WATERCONTENT-33KPA_USDA-4B1C_M/v01"]



eeauth(service_account,p_key)

region = draw_region_rect(lat, lon)

#%%
#load all layers

from ee_functions import gsw_reclass,awc_reclass,make_potinfil

gsw = ee.Image(layers[1]).select("occurence").clip(region)

tex = ee.Image(layers[2]).select("b0").clip(region)
awc = ee.Image(layers[3]).select("b0").clip(region)

nw_gsw = gsw_reclass(gsw)
nw_awc = awc_reclass(awc)
pot_infil,high_only = make_potinfil(tex)


tex_map = geemap.Map(center=(lon, lat), zoom=4,toolbar_ctrl=True, layer_ctrl=True)
tex_map.addLayer(high_only,{},"infil_modified",True,0.8)
#%%
tex_map.save("out.html")