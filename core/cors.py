# -*- coding: utf-8 -*-
# Author :  #Bitwis3 - Hamid Mahmoud -

from core.colors import *
import requests

# Check Cross Origin Weakness
def CheckCORS(site,origin_site):
    hdr = {'Origin':'{0}'.format(origin_site)}
    try:
        response = requests.get(site, headers=hdr,timeout=3)
        res_headers = response.headers
        if 'Access-Control-Allow-Origin' in response.headers:
            if response.headers['Access-Control-Allow-Origin'] == origin_site or response.headers['Access-Control-Allow-Origin'] == '*':
                return (Y+'['+R+'+'+Y+'] ['+W+'CORS'+G+'] Target: '+str(site).rstrip()+' is Vulnerable!'+G)
        else:
            return (G+'['+W+'+'+G+'] ['+W+'CORS'+G+'] Target: '+str(site).rstrip()+' is '+B+'not'+G+' Vulnerable!'+G)
    except requests.Timeout as err:
        pass

