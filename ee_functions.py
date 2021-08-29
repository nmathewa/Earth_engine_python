"""
Created on Thu May  6 17:58:31 2021

@author: mathew

"""
import ee


def draw_region_rect(lat,lon):
    lonmin = lon - 10
    lonmax = lon + 10
    latmin = lat - 10
    latmax = lat + 10
    region = ee.Geometry.Rectangle(lonmin, latmin, lonmax, latmax)
    return region


def load_multi(in_layers,geometry):
    ld_layer = []
    for ii in in_layers:
        ld_layer += [ee.Image(ii).clip(geometry)]
    return ld_layer


def gsw_reclass(gsw):
    ma = 100
    recl_ras = gsw.expression('b(0) <= 10 ? 1 : b(0) < 20 ? 2 : b(0) <= 30 ? 3 : b(0) <= 40 ? 4 : b(0) <= 50 ? 5 : b(0) <= 60 ? 6 : b(0) <= 70 ? 7 : b(0) <= 80 ? 8 : b(0) <= 90 ? 9 : b(0) <= 100 ? 10 : 0')
    return recl_ras    


def awc_reclass(awc):
    max_ = 54
    recl_ras_awc = awc.expression('b(0) <= '+str(max_*0.1)+' ? 1 : b(0) < '+str(max_*0.2)+' ? 2 : b(0) <= '+str(max_*0.3)+' ? 3 : b(0) <= '+str(max_*0.4)+' ? 4 : b(0) <= '+str(max_*0.5)+' ? 5 : b(0) <= '+str(max_*0.6)+' ? 6 : b(0) <= '+str(max_*0.7)+' ? 7 : b(0) <= '+str(max_*0.8)+' ? 8 : b(0) <= '+str(max_*0.9)+' ? 9 : b(0) <= '+str(max_)+' ? 10 : 0')
    return recl_ras_awc

def make_potinfil(texture_map):
    recl_ras_tex = texture_map.expression('b(0) == 1 ? 0.15 : b(0) == 2 ? 0.15 : b(0) == 3 ? 0.51 : b(0) == 4 ? 0.15 : b(0) == 5 ? 0.15 : b(0) == 6 ? 0.51 : b(0) == 7 ? 0.15 : b(0) == 8 ? 1.14 : b(0) == 9 ? 0.51 : b(0) == 10 ? 0.51 : b(0) == 11 ? 1.14 : b(0) == 12 ? 2.03 : 0')
    recl_high_infil = recl_ras_tex.expression('b(0) >= 2 ? 1 :0').selfMask()
    return recl_ras_tex,recl_high_infil

def Lrun_highAwc(reclass_run,reclass_awc):
    comb = reclass_run.eq(1).And(reclass_awc.eq([5,6,7,8,9,10]))
    #bare_img = ee.Image(comb).select('constant').selfMask()
    bare_img = ee.Image(comb).select('constant').selfMask()
    return bare_img

