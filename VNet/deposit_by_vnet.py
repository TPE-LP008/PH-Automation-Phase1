# coding=UTF-8

from selenium import webdriver									# 導入webdriver包
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import random


''' 生成隨機n位數'''
def get_random_int(digits):
	rand_num = ""
    for i in range(digits):
		ch = chr(random.randrange(ord('0'), ord('9') + 1))
		rand_num += ch

	return rand_num


def deposit_by_vnet():
	driver.find_element_by_css_selector("li[onclick*='mockvnc']").click()
    driver.find_element_by_name("mer_id").click()
    driver.find_element_by_css_selector("option[value='MQA00001']").click()		# Merchant ID: MQA00001
    driver.find_element_by_name("cust_tag").send_keys(get_random_int(6))
    driver.find_element_by_name("txn_amt").clear()
    deposit = get_random_int(4)
    driver.find_element_by_name("txn_amt").send_keys(deposit)
    print("deposit amount is $" + str(int(deposit)/100))
    driver.find_element_by_name("Submit").click()
    driver.find_element_by_name("btn_buyCard").click()
    driver.find_element_by_name("card_type_debit").click()					# Debit Card
    """
    工商銀行 (086102) / 招商銀行 (086308) / 農業銀行 (086103) / 建設銀行 (086105) / 中國銀行 (086104) / 民生銀行 (086305) / 
    興業銀行 (086309) / 浦東發展銀行 (086310) / 交通銀行 (086301) / 中信銀行 (086302) / 光大銀行 (086303) / 華夏銀行 (086304) / 
    發展銀行 (086306) / 平安銀行 (086502) / 北京銀行 (086501) / 郵政儲蓄銀行 (086403) / 上海銀行 (086507) / 農村商業銀行 (086517)
    """
    driver.find_element_by_css_selector("input[value='086302']").click()		# 中信銀行
    # driver.find_element_by_id("debit_bank_id_9").click()					# 排序為第9的銀行
    driver.find_element_by_id("btn_submit").click()

    driver.find_element_by_css_selector("input[value*='Success']").click()		# 模擬成功
    # driver.find_element_by_css_selector("input[value*='Failed']").click()		# 模擬失敗


driver = webdriver.Ie()					# 初始化一个IE浏览器实例：driver
driver.maximize_window()				# 瀏覽器最大化
driver.implicitly_wait(6)				# 設置隱式時間等待 (最長等待時間, 如果在規定時間內網頁加載完成, 則執行下一步, 否則一直等到時間截止。 注意這裡有一個弊端, 那就是程式會一直等待整個頁面加載完成。)

T1 = time()

# Login Mock
driver.get("http://mock.systest.site/sdprod/")
driver.find_element_by_id("mockpwd").send_keys("mockpwd\n")
deposit_by_vnet()
print("Cost time is " + str(time() - T1))		# 耗時多久

sleep(3)
driver.quit()
