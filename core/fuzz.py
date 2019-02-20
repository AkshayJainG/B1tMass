# -*- coding: utf-8 -*-
# Author :  #Bitwis3 - Hamid Mahmoud -

from concurrent import futures
from core.colors import *
import requests

domList = []
gSit = ""

# Single Fuzzing 
def FuzzThis(pay):
    global gSit
    test = gSit
    try:
        response = requests.get(test+str(pay).rstrip(),timeout=3)
        if response.status_code == 200 and len(response.history) == 0 and "Sorry" not in response.text:
            #if str(pay).rstrip().lower() in response.text.lower():
            print(Y+'['+R+'+'+Y+'] Target: '+str(test).rstrip()+' File '+R+'Found!!! '+Y+'['+B+str(pay).rstrip()+G+']'+G)
        else:
            print(Y+'['+R+'-'+Y+'] Target: '+str(test).rstrip()+G+' File Not Found!'+G)

    except requests.Timeout as err:
        pass


# Check file
def FuzzEx(site):
    global gSit
    gSit = site
    f = open('core/fuzz.txt','r')
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
                res = executor.map(FuzzThis,domList)

