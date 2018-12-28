# -*- coding: utf-8 -*-
# Author :  #Bitwis3 - Hamid Mahmoud -

from concurrent import futures
from core.colors import *
import requests

domList = []
gSit = ""

# Single Injection
def InjectDom(domVar):
    global gSit
    test = gSit
    try:
        response = requests.get(test+str(domVar).rstrip(),timeout=3,verify=False)
        if str(domVar).rstrip() in response.text:
            print(Y+'['+R+'+'+Y+'] Target: '+str(test).rstrip()+' is '+R+'Vulnerable'+Y+' to DOM XSS  ['+R+str(domVar).rstrip()+G+']'+G)
        else:
            print(Y+'['+R+'+'+Y+'] Target: '+str(test).rstrip()+' is'+B+' not'+Y+' Vulnerable to DOM XSS ['+R+str(domVar).rstrip()+G+']'+G)

    except requests.Timeout as err:
        pass


# Check DOM XSS from a file
def DOMInjection(site):
    global gSit
    gSit = site
    f = open('core/dom.txt','r')
    countIter = 0
    try:
        domList = f.readlines()
    except:
        pass
    finally:
        f.close()
        if len(domList) > 0:
            workers = min(30,len(domList))
            with futures.ThreadPoolExecutor(workers) as executor:
                res = executor.map(InjectDom,domList)

