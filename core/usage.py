import argparse


# Handling CommandLine Arguments
parser = argparse.ArgumentParser(description='Multiple Weaknesses Checking for Mass Subdomains')
parser.add_argument('-f', '--file', help='Subdomains File Path', dest='file')
parser.add_argument('-O', '--origin', help='Origin Tag to be Injected', dest='origin')
parser.add_argument('-c', '--cors',action="store_true",default=False, help='Skip CORS Checking', dest='nocors')
parser.add_argument('-m', '--mobile',action="store_true",default=False, help='Mobile Mode', dest='mobile')
parser.add_argument('-H', '--headers', action="store_true",default=False,help='Skip Headers Injection Checking', dest='nohead')
parser.add_argument('-D', '--dom', action="store_true",default=False,help='Skip DOM XSS Checking', dest='nodom')
parser.add_argument('-t', '--threads', help='Number of Threads',dest='threadnumbers', type=int, default=10)
parser.add_argument('-z', '--fuzz', action="store_true",default=False,help='File/s Searching',dest='fuzz')
args = parser.parse_args()


