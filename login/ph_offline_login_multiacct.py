import unittest
import os
import time
from selenium import webdriver

#Read the account/password file
f = open(r'C:/Users/johnson.l/Desktop/py_se/pw.txt')
text = []
for line in f:
    text.append(line)
f.close()
max = len(text)

def readfile(i):
    
    global account
    global pw
    global name
    f = open(r'C:/Users/johnson.l/Desktop/py_se/pw.txt')
    text = []
    for line in f:
        text.append(line)
    f.close()

    account = text[i].strip('\n')
    pw = text[i+1].strip('\n') 
    name = text[i+2].strip('\n')
    print("Count:",i,account,pw,name)
    

# navigate to the application home page
def login():
    dir = os.getcwd()
    ie_driver_path = dir + '\IEDriverServer.exe'

    # create a new Internet Explorer session
    driver = webdriver.Ie(ie_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()

    driver.get('https://pholadminsd.pd.local/admin/auth/login')

    #For IE 
    driver.find_element_by_link_text("其他資訊").click()
    driver.find_element_by_link_text("繼續瀏覽網頁 (不建議)").click()

    #Login page
    driver.find_element_by_id("UserLoginForm_username").clear()
    driver.find_element_by_id("UserLoginForm_username").send_keys(account[8:])
    driver.find_element_by_id("UserLoginForm_password").clear()
    driver.find_element_by_id("UserLoginForm_password").send_keys(pw[3:])
    driver.find_element_by_name("yt0").click()

    #Logout process
    driver.find_element_by_link_text("Account (" + name[5:] + ")").click()
    driver.find_element_by_link_text("Logout (" + name[5:] + ")").click()

    driver.delete_all_cookies()
    driver.quit()
    time.sleep(2)

for i in range(0,max,3):
    readfile(i)
    login()
