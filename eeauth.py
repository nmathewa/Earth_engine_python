"""
Created on Thu May  6 18:35:02 2021

@author: mathew

"""

import geeadd
import ee


def eeauth(ac_name,public_key):
    p_key = public_key
    service_account = ac_name
    credentials = ee.ServiceAccountCredentials(service_account, p_key)
    ee.Initialize(credentials)

p_key = "/home/mathew/hdd/UBU20/hdd/TCR/GIT/StopRunoff/assets/geengine-312606-81c6465d7301.json"
service_account = 'geengine@geengine-312606.iam.gserviceaccount.com '
credentials = ee.ServiceAccountCredentials(service_account, p_key)
ee.Initialize(credentials)
#%%
#import geeup

#geeup.tabup()