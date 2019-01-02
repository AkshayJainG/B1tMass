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
from core.usage import *

import requests
import validators
import sys
import os


targets = str(args.file)
origin_site = str(args.origin)
MAX_WORKERS = int(args.threadnumbers)
validSites = []
isUPList = []



# Check Live Hosts
def IsUP(site):
    global args
    try:
        req = requests.head(site,timeout=3)
        if args.nocors:
            print(CheckCORS(site,origin_site))
        if args.nohead:
            HeadInjection(site,'WOOTWOOT',MAX_WORKERS)
        if args.nodom:
            DOMInjection(site)
        isUPList.append(site)
    except Exception as e:
        pass


# Fetch Targets from the File
def GetTargets():
    global parser
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
        parser.print_help()
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
    global args
    m = args.mobile
    if m:
        print("""%s
                    Mobile Mode
                     #B1tMass
                %s%s"""%(W,W,G))
    if not m:
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
