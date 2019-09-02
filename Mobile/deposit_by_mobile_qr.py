# coding=UTF-8

from selenium import webdriver
from time import sleep, time
from PIL import Image
import pyzbar.pyzbar as pyzbar
import random


# 生成隨機 n 位數
def get_random_int(digits):
    rand_num = ""

    for i in range(digits):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        rand_num += ch

    return rand_num


# 讀取QR Code
def load_qr_info():
    driver.save_screenshot("/SD/QR-Code.png")       # 網頁視窗截圖

    # 確認可讀取QR Code的資訊
    notFound = True
    while notFound:
        barcodes = pyzbar.decode(Image.open("/SD/QR-Code.png"))
        if len(barcodes):
            notFound = False

    barcodeData = barcodes[0].data.decode("utf-8")
    return barcodeData


# 支付Service - Mobile - QR Code
def deposit_by_mobile_qr():
    driver.find_element_by_xpath("//b[contains(text(), 'Mobile Mock Merchant')]").click()
    driver.find_element_by_css_selector("select#mer_id").click()
    driver.find_element_by_css_selector("option[value='MQA00005']").click()        # MerchantID: MQA VMOBILE2
    driver.find_element_by_css_selector("td.nnormal>input#cust_tag").send_keys(get_random_int(6))      # 亂數生成Customer Tag
    driver.find_element_by_css_selector("input#txn_amt").clear()
    driver.find_element_by_css_selector("input#txn_amt").send_keys(get_random_int(4))      # 亂數生成deposit amount
    # PSP Account ID: driver.find_elements_by_css_selector("select#selected_pid[name='selected_pid']").click()
    # Bank Code: driver.find_elements_by_css_selector("select#bank_code").click()
    driver.find_element_by_css_selector("input#Submit").click()
    driver.find_element_by_css_selector("input.nnormal[name='mobileno']").clear()
    driver.find_element_by_css_selector("input.nnormal[name='mobileno']").send_keys("11111111111")
    driver.find_element_by_css_selector("input[value='086097']").click()        # 掃碼支付: 086097
    driver.find_element_by_css_selector("tr>td>input.btnSubmit[type='submit']").click()
    """driver.find_element_by_css_selector("input#086081").click()     ID不支援'#'後面接數字的用法 => invalid or illegal selector"""
    driver.find_element_by_css_selector("input[id='086081']").click()      # 086081: 微信支付 / 086082: QQ錢包 /  086083: 支付寶 /  086084: 銀聯二維碼支付
    driver.find_element_by_css_selector("input#btn[type='submit']").click()
    # 讀取QR Code
    confirm_page = load_qr_info()
    # 開啟二維碼內藏的網址
    js = 'window.open("' + confirm_page + '");'
    driver.execute_script(js)
    handles = driver.window_handles
    driver.switch_to_window(handles[-1])
    driver.find_element_by_css_selector("input#btn_yes[value*='Success']").click()


driver = webdriver.Ie()
driver.maximize_window()
driver.implicitly_wait(6)

T1 = time()

# Login Mock
driver.get("http://mock.systest.site/sdprod/")
driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
deposit_by_mobile_qr()

print("Cost time is " + str(time() - T1))

sleep(2)

driver.close()
driver.quit()
