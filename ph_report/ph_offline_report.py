import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#Read the account/password file
f = open(r'C:/Users/johnson.l/Desktop/py_se/pw.txt')
text = []
for line in f:
    text.append(line)
f.close()
account = text[0].strip('\n')
pw = text[1].strip('\n') 
name = text[2].strip('\n')


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
        self.driver.find_element_by_link_text("其他資訊").click()
        self.driver.find_element_by_link_text("繼續瀏覽網頁 (不建議)").click()
    
   #Login process
    def test_LogIN(self):
        self.driver.find_element_by_id("UserLoginForm_username").clear()
        self.driver.find_element_by_id("UserLoginForm_username").send_keys(account[8:])
        self.driver.find_element_by_id("UserLoginForm_password").clear()
        self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw[3:])
        self.driver.find_element_by_name("yt0").click()
                
    #Make sure that Login success
        msg = self.driver.find_element_by_id("headerText").text
        if msg == "Admin Console (SD Prod) - Offline":
            print(" ***** Login Pass! *****")
        else:
            print(" ***** Login Failed! *****")
        self.driver.close()
    
    #Logout process
    def test_LogOUT(self):    
        self.driver.find_element_by_id("UserLoginForm_username").clear()
        self.driver.find_element_by_id("UserLoginForm_username").send_keys(account[8:])
        self.driver.find_element_by_id("UserLoginForm_password").clear()
        self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw[3:])
        self.driver.find_element_by_name("yt0").click()
        self.driver.find_element_by_link_text("Account (" + name[5:] + ")").click()
        self.driver.find_element_by_link_text("Logout (" + name[5:] + ")").click()
        
    #Make sure that Logout success
        mes = self.driver.find_element_by_id("logo2").text
        if mes == "Admin Console (OfflineProduction)":
            print(" ***** Logout Pass! *****")
        else:
            print(" ***** Logout Failed! *****")
        self.driver.close()

    def test_bankaccount(self):
    #Creat the bank accout, "Remark" needs unique!!
        self.driver.find_element_by_id("UserLoginForm_username").clear()
        self.driver.find_element_by_id("UserLoginForm_username").send_keys(account[8:])
        self.driver.find_element_by_id("UserLoginForm_password").clear()
        self.driver.find_element_by_id("UserLoginForm_password").send_keys(pw[3:])
        self.driver.find_element_by_name("yt0").click()
        self.driver.find_element_by_link_text("Provider").click()
        self.driver.find_element_by_link_text("Bank Account Management").click()
        self.driver.find_element_by_link_text("Create").click()
    
    #Fill in the data for account
        select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_INIT_PROVIDER_ID]'))
        select.select_by_visible_text("IT Provider A")
        select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_INT_BANK_CODE]'))        
        select.select_by_visible_text("建设银行")
        self.driver.find_element_by_id("OfflineBankAccount_OB_BANK_ACCT_NUM").send_keys(2882019201914)
        select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_ACCT_CCY]'))  
        select.select_by_visible_text("CNY")
        select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_ACCT_TYPE]'))
        select.select_by_visible_text("Deposit")
        self.driver.find_element_by_name("OfflineBankAccount[OB_OWNER_NAME]").send_keys("auto_test")
        self.driver.find_element_by_name("OfflineBankAccount[OB_PROVINCE]").send_keys("auto_test")
        self.driver.find_element_by_name("OfflineBankAccount[OB_CITY]").send_keys("auto_test")
        self.driver.find_element_by_name("OfflineBankAccount[OB_BRANCH_NAME]").send_keys("auto_test")
        select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_SYS_SWITCH_ENABLED]'))
        select.select_by_visible_text("Enable")
        select = Select(self.driver.find_element_by_name('OfflineBankAccount[OB_SUPPORT_SMS_STMT]'))        
        select.select_by_visible_text("Enable")
        #Special remark string for search!
        self.driver.find_element_by_name("OfflineBankAccount[OB_REMARK]").send_keys("lee004")
        self.driver.find_element_by_id("OfflineBankAccount_OB_RECEIVED_DATETIME").send_keys("2019-01-02")
        self.driver.find_element_by_name("yt0").click()
        time.sleep(2)
                
    #Switch to pop out window
        self.yes = self.driver.switch_to.alert
        self.yes.accept()
        time.sleep(3)

    #Back to Bank Account Management page
        self.driver.find_element_by_link_text("Provider").click()
        self.driver.find_element_by_link_text("Bank Account Management").click()

    #Search the account and change the status to Active
        self.driver.find_element_by_link_text("Advanced Search").click()
        self.driver.find_element_by_name("OfflineBankAccount[OB_REMARK]").send_keys("lee004")
        self.driver.find_element_by_id("btn_Search").click()
        time.sleep(2)
        self.driver.find_element_by_id("SELECT_ACCT_NUM").click()
        self.driver.find_element_by_id("batch-update-account-btn").click()
        select = Select(self.driver.find_element_by_name('BANK_ACCT_STATUS'))
        select.select_by_visible_text("Active")
        time.sleep(2)
        self.driver.find_element_by_id("batch-update-btn").click()
        self.yes_active = self.driver.switch_to.alert
        self.yes_active.accept()
        time.sleep(2)
        
    #Back to Bank Account Management page
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_link_text("Provider").click()
        self.driver.find_element_by_link_text("Bank Account Management").click()
        self.driver.find_element_by_link_text("Advanced Search").click()
        self.driver.find_element_by_name("OfflineBankAccount[OB_REMARK]").send_keys("lee004")
        self.driver.find_element_by_id("btn_Search").click()
        #self.driver.find_element_by_id("quickViewBtn").click()
        time.sleep(3)
    
    #Catch the status of the bank account and check the status is Active or not
        b_acct = self.driver.find_element_by_xpath("//*[@id='offline-bank-account-grid']/table/tbody/tr/td[4]").text
        b_status = self.driver.find_element_by_xpath("//*[@id='offline-bank-account-grid']/table/tbody/tr/td[13]").text
        print("Bank account is created. \nBank account number is: " + b_acct + " The status is: "+ b_status)
    #Status is active => pass, else => failed
        self.assertEqual(b_status,"Active",msg="Ths status is not Acticve now!")
        time.sleep(3)

    #End the test, close the browser window
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
