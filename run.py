__author__ = 'Bernardo Godinho'

import csv
import mechanize
import re
import time
import BeautifulSoup
import smtplib
import cookielib
import os
import inemail
import time


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BACK_LRED = '\033[101m' 

def checkForToA(username, password):
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)
    browser.addheaders = [('User-agent', 'Firefox')]
    start = 0
    continuar = True
    links = []

    print("Connecting: ")
    print("\tUsername: "+username)

    browser.open("https://mycusthelp.info/IIE/_cs/Login.aspx")
    browser.select_form(nr=0)
    browser.form['txtUsername'] = username
    browser.form['txtPassword'] = password
    response1 = browser.submit()
    html = response1.read() + "dsas"
    
    print("\tPrograms")

    browser.open("https://mycusthelp.info/IIE/_cs/COList.aspx?fid=5")
    #
    
    html = browser.response().get_data()

    

    html = html[html.index("Brazil") - 100: html.index("Brazil")].replace("'id'",  "  'id'")

    m = re.match("[^\"]*\W*id[^:]*:\D*(\d+)", html)
    aa = ""
    if m:
        aa = m.group(1)
    
    print("\tBSWB Id: " + str(aa))    

    browser.open("https://mycusthelp.info/IIE/_cs/CODetails.aspx?ot=2&fid=5&oi=" + str(aa))


    html = browser.response().get_data()

    if "passport" in html.lower():
        print("\tPassport: OK") 

    
    if html.count('erms') > 2:
        return True
        print "\tToA!!!"
        inemail.sendEmail("TOA", *cred)
        
    else:
        return False
        

        #inemail.sendEmail("No TOA", *cred)


while True:
    emailCred = 'email@gmail.com', 'senhaEmail'
    userPwd = emailCred[0], 'senhaIIE'
    if checkForToA(*userPwd):
        print bcolors.BACK_LRED + "\tToA: Yes" + bcolors.ENDC
        inemail.sendEmail("TOA", *emailCred)
    else:
        print bcolors.OKBLUE + "\tToA: No" + bcolors.ENDC

    print("\tSleeping for 50\n\n")    
    time.sleep(50)
    
