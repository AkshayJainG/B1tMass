#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author :  #Bitwis3 - Hamid Mahmoud -

from urllib.parse import urlparse
from concurrent import futures

#Importing custom libs
from core.cors import *
from core.colors import *
from core.headers import *
from core.dom import *

import requests
import validators
import sys
import os

targets = str(sys.argv[1])
origin_site = str(sys.argv[2])
MAX_WORKERS = 10
validSites = []
isUPList = []


# Checking Arguments
if len(sys.argv) < 2:
    sys.exit(R+"[-] Check Arguments!"+G)


# Check Live Hosts
def IsUP(site):
    try:
        req = requests.get(site,timeout=3)
        print(CheckCORS(site,origin_site))
        HeadInjection(site,'WOOTWOOT')
        DOMInjection(site)
        isUPList.append(site)
    except Exception as e:
        pass


# Fetch Targets from the File
def GetTargets():
    print(Y+'['+R+'*'+Y+'] Loading Targets.....'+G)
    target = None
    try:
        target = open(targets,'r')
        print(Y+"["+R+"+"+Y+"] Targets were Loaded"+G)
        print(Y+"["+R+"*"+Y+"] Start Checking, Please Wait.\n"+G)
        for site in target:
          check = validators.url(site)
          parser = urlparse(site)
          if check:
              validSites.append(str(site).rstrip())
    except:
        pass
    finally:
        if target is not None:
            target.close()

        if len(validSites) > 0:
            workers = min(MAX_WORKERS, len(validSites))
            with futures.ThreadPoolExecutor(workers) as executor:
                res = executor.map(IsUP, validSites)


# Main Features
def Features():
    f = open("core/features.txt","r")
    print(G+'['+W+'~'+G+']'+R+' Main Features :'+G)
    try:
        for feature in f:
            print(G+'['+Y+'~'+G+']'+W+' \t'+str(feature).rstrip()+G)
    except:
        pass
    finally:
        print("\n")
        f.close()

# Banner
def welcome():
    print("""%s
                ██████╗  ██╗████████╗███╗   ███╗ █████╗ ███████╗███████╗
                ██╔══██╗███║╚══██╔══╝████╗ ████║██╔══██╗██╔════╝██╔════╝
                ██████╔╝╚██║   ██║   ██╔████╔██║███████║███████╗███████╗
                ██╔══██╗ ██║   ██║   ██║╚██╔╝██║██╔══██║╚════██║╚════██║
                ██████╔╝ ██║   ██║   ██║ ╚═╝ ██║██║  ██║███████║███████║
                ╚═════╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝


                                                                     %s%s
                          # Developed by Bitwis3
                            # B1tMass Testing
    """ % (W, W, G))

if __name__ == "__main__":
    os.system('reset')
    welcome()
    Features()
    GetTargets()
