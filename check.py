#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : @fasthm00 #Bitwis3 - Hamid Mahmoud -

from urllib.parse import urlparse
import requests
import validators
import sys
import json
import os
import socket

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[97m'  # white

targets = str(sys.argv[1])
origin_site = str(sys.argv[2])
port = 80
if len(sys.argv) < 2:
    sys.exit(R+"[-] Check Arguments!"+G)


def IsUP(site):
    try:
        req = requests.get(site)
        return True
    except:
        return False

def GetTargets():
    print(Y+'[*] Loading Targets.....'+G)
    target = None
    try:
        target = open(targets,'r')
        print(Y+"[+] Targets Have Been Loaded"+G)
        print(Y+"[*] Start Checking, Please Wait.\n"+G)
        for site in target:
          check = validators.url(site)
          parser = urlparse(site)
          if check:
              if IsUP(site):
                  CheckCORS(site)
    except Exception as e:
        print(R+str(e)+G)
    finally:
        if target is not None:
            target.close()

def CheckCORS(site):
    #print(B+"[*] Checking Target: "+site+G)
    hdr = {'Origin':'{0}'.format(origin_site)}
    try:
        response = requests.get(site, headers=hdr,timeout=3)
        res_headers = response.headers
        if 'Access-Control-Allow-Origin' in response.headers:
            if response.headers['Access-Control-Allow-Origin'] == origin_site or response.headers['Access-Control-Allow-Origin'] == '*':
                print(Y+'[+] Target: '+str(site).rstrip()+' is Vulnerable!'+G)
        else:
            print(G+'[+] Target: '+str(site).rstrip()+' is not Vulnerable!'+G)
    except requests.Timeout as err:
        pass



def welcome():
    print("""%s
            ███╗   ███╗ █████╗ ███████╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗
            ████╗ ████║██╔══██╗██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
            ██╔████╔██║███████║███████╗███████╗██║     ██║   ██║██████╔╝███████╗
            ██║╚██╔╝██║██╔══██║╚════██║╚════██║██║     ██║   ██║██╔══██╗╚════██║
            ██║ ╚═╝ ██║██║  ██║███████║███████║╚██████╗╚██████╔╝██║  ██║███████║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

                                                                     %s%s
                          # Developed by Bitwis3
                            # Mass CORS Testing
    """ % (W, W, G))

if __name__ == "__main__":
    welcome()
    GetTargets()
