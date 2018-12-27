# -*- coding: utf-8 -*-
# Author :  #Bitwis3 - Hamid Mahmoud -

from concurrent import futures
from core.colors import *
import requests

headList = []
gsite = ""
gpayload = ""

# Single Injection
def InjectHead(headVar):
    global gpayload
    global gsite
    test = gsite
    hdr = {str(headVar).rstrip():str(gpayload)}
    try:
        response = requests.get(test, headers=hdr,timeout=3)
        res_headers = response.headers
        if str(headVar).rstrip() in response.headers:
            if response.headers[str(headVar).rstrip()] == gpayload :
                print(Y+'['+R+'+'+Y+'] Target: '+str(test).rstrip()+' is '+R+'Vulnerable'+Y+' to Header Injection ['+R+str(headVar).rstrip()+G+']'+G)
        else:
            print(Y+'['+R+'+'+Y+'] Target: '+str(test).rstrip()+' is'+B+' not'+Y+' Vulnerable to Header Injection ['+R+str(headVar).rstrip()+G+']'+G)

    except requests.Timeout as err:
        pass


# Check Header Injection with a given Payload
def HeadInjection(site,payload):
    global gsite,gpayload
    gsite = site
    gpayload = payload
    f = open('core/headers.txt','r')
    countIter = 0
    try:
        headList = f.readlines()
    except:
        pass
    finally:
        f.close()
        if len(headList) > 0:
            workers = min(50,len(headList))
            with futures.ThreadPoolExecutor(workers) as executor:
                res = executor.map(InjectHead,headList)


