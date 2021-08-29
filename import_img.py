"""
Created on Thu May  6 18:11:52 2021

@author: mathew

"""
import geemap
import ee
import os

os.system("earthengine authenticate")

#%%
def create_map(region):
    i_map = geemap.Map(center=(lon, lat), zoom=4,toolbar_ctrl=True, layer_ctrl=True)
    return i_map
    
def load_maps(map_names):
    ld_maps = []
    for ii in map_names:
        ld_maps += [ee.Image(ii)]
    
    return ld_maps

