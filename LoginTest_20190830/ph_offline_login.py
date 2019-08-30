import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

TC1 = []
TC2 = []
TC3 = []
TC4 = []

if os.path.isfile('accpw.csv'):
    print('找到目標檔案 accpw.csv')
    #讀取檔案
    with open('accpw.csv', 'r',encoding = 'utf-8', errors = "ignore") as f:
        for line in f:
			# if 'login' in line: continue #繼續,跳到下一迴()
            s = line.strip().split(',') # split(',')就是遇到','就切一刀下去變成兩個欄位
            case = s[0]
            item = s[1]
            data = s[2]
            if case == 'login':
                TC1.append([item, data])
            elif case == 'blank':
                TC2.append([item, data])
            elif case == 'invalid':
                TC3.append([item, data])
            elif case == 'repeat':
                TC4.append([item, data])

def settc1(i):
    global acct, pw, name
    acct     = TC1[i][1]
    pw       = TC1[i+1][1]
    name     = TC1[i+2][1]

def settc2(i):
    global acct2, pw2
    acct2     = TC2[i][1]
    pw2       = TC2[i+1][1]

def settc3(i):
    global acct3, pw3
    acct3     = TC3[i][1]
    pw3       = TC3[i+1][1]
    
def settc4(i):
    global acct4, pw4, name4
    acct4     = TC4[i][1]
    pw4       = TC4[i+1][1]
    name4     = TC4[i+2][1]

class LoginTests(unittest.TestCase):

    #initiation for the test
    def setUp(self):
        dir = os.getcwd()
        ie_driver_path = dir + '\IEDriverServer.exe'
        # create a new Internet Explorer session
        self.driver = webdriver.Ie(ie_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://pholadminsd.pd.local/admin/auth/login')

        #For IE Only
        self.setUpdriver.find_element_by_xpath("//*[@id='moreInfoContainer']/A").click()
        self.driver.find_element_by_xpath("//*[@id='overridelink']").click()
    
   #Login process
    def test_LogIN(self):
        for i in range(0,len(TC1),3):
            settc1(i)
            self.driver.find_element_by_id("UserLoginForm_username").clear()
            self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
            self.driver.find_element_by_id("UserLoginForm_password").clear()
            self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
            self.driver.find_element_by_name("yt0").click()
            
        #Make sure that Login success
            msg = self.driver.find_element_by_id("headerText").text
            if msg == "Admin Console (SD Prod) - Offline":
                print(" ***** Login Pass! *****")
            else:
                print(" ***** Login Failed! *****")
            self.driver.close()
    
    # #Logout process
    def test_LogOUT(self):
        for i in range(0,len(TC1),3):
            settc1(i)
            self.driver.find_element_by_id("UserLoginForm_username").clear()
            self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct)
            self.driver.find_element_by_id("UserLoginForm_password").clear()
            self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw)
            self.driver.find_element_by_name("yt0").click()
            self.driver.find_element_by_link_text("Account (" + name + ")").click()
            self.driver.find_element_by_link_text("Logout (" + name + ")").click()
            
        #Make sure that Logout success
            mes = self.driver.find_element_by_id("logo2").text
            if mes == "Admin Console (OfflineProduction)":
                print(" ***** Logout Pass! *****")
            else:
                print(" ***** Logout Failed! *****")
            self.driver.close()
    
    # account = blank, pw = blank, both account&pw blank
    def test_Error_blank(self):
            for i in range(0,len(TC2),2):
                settc2(i)
                self.driver.find_element_by_id("UserLoginForm_username").clear()
                self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct2)
                self.driver.find_element_by_id("UserLoginForm_password").clear()
                self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw2)
                self.driver.find_element_by_name("yt0").click()
                
                E_msg = self.driver.find_element_by_class_name("errorSummary").text
                self.assertIn("cannot be blank",E_msg, msg="Error message wrong!")
                print("Case: ")
                print("Account: "+acct2+" password: "+pw2)
                print("Error message: " + "\n" + E_msg)
            
            self.driver.close()
    
    #account = blank, pw = blank, both account&pw blank
    def test_Error_invalid(self):
            for i in range(0,len(TC3),2):
                settc3(i)
                self.driver.find_element_by_id("UserLoginForm_username").clear()
                self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct3)
                self.driver.find_element_by_id("UserLoginForm_password").clear()
                self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw3)
                self.driver.find_element_by_name("yt0").click()
                
                E_msg = self.driver.find_element_by_class_name("errorSummary").text
                self.assertIn("combination invalid.",E_msg, msg="Error message wrong!")
                print("Case: ")
                print("Account: "+acct3+" password: "+pw3)
                print("Error message: "+ "\n" + E_msg)
            self.driver.close()
    
    def test_loginloop(self):
            count = 0
            for i in range(0,len(TC4),3):
                settc4(i)
                self.driver.find_element_by_id("UserLoginForm_username").clear()
                self.driver.find_element_by_id("UserLoginForm_username").send_keys(acct4)
                self.driver.find_element_by_id("UserLoginForm_password").clear()
                self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw4)
                self.driver.find_element_by_name("yt0").click()
                self.driver.find_element_by_link_text("Account (" + name4 + ")").click()
                self.driver.find_element_by_link_text("Logout (" + name4 + ")").click()
                count +=1
                print("\n"+"Test:" + str(count) + "\n" +"Account: "+acct4+" password: "+pw4)
            print("Number of login/logout test: "+ str(count))
            

    #End the test, close the browser window
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
