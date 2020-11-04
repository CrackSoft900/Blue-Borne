#!/usr/bin/env python
try:
    from datetime import datetime
    import os
    import hashlib
    import sys
    import time
    import threading
    import string
    import random
    import base64
    import urllib.request
    import urllib.parse
    import subprocess
    import webbrowser
    import smtplib
    import sys
    import os
    import subprocess
    import json
    import notify2
     
except :
    print("Plase Install Require Package \nUsing 'pip install -r requirement.txt'")


Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
verl = open("core/.version", 'r').read()

def startM():
    try:
        notify2.init('HPomb Tool')
        n = notify2.Notification("HPomb Tool",
                                 "Mail Bombing Start",
                                 ""
                                )
        n.show()
        n.timeout = 50000
        print("\a")
    except:
        print("Sorry Notification Feature Not For You")


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def banner():
    
    clr()
    logo="""
 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗ ██████╗ ███████╗████████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔═══██╗██╔════╝╚══██╔══╝
██║     ██████╔╝███████║██║     █████╔╝ ███████╗██║   ██║█████╗     ██║   
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ╚════██║██║   ██║██╔══╝     ██║   
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████║╚██████╔╝██║        ██║   
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝        ╚═╝   
-by Shlok Kesarwani & Hacker-CrackSoft



               ""","""
----------------   ----------------------
| KLS  Project |   | Version : """,verl,""" |
----------------   ----------------------

"""
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3])

clr()
banner()
