import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By


def test_method():
    chrome_driver = webdriver.Chrome(r"C:\Users\O'Brands\Desktop\space\chromedriver_win32\chromedriver.exe")
    chrome_driver.get('https://tbcpay.ge/')
    chrome_driver.maximize_window()
    action = ActionChains(chrome_driver)
    wait = WebDriverWait(chrome_driver, 10)
    # head_navigation
    for x in range(2, 6):
        chrome_driver.find_element_by_xpath("//*[@class='container flex-start']/a[" + str(x) + "]")
    # service_navigation
    for x in range(1, 10):
        chrome_driver.find_element_by_xpath("//*[@class='sc-179zpai-0 kLtDrh']/li[" + str(x) + "]")
    # search_field
    input_search = chrome_driver.find_element_by_xpath("//*[@class='sc-1pux4l1-0 jRUCjy']/form/input")
    submit = chrome_driver.find_element_by_xpath("//*[@class='sc-1pux4l1-0 jRUCjy']/form/button")
    # search_mobile
    input_search.send_keys("მობილური")
    # check if "ბალანსის შევსება" exist
    balance = chrome_driver.find_element_by_xpath("//*[@class='sc-13q1cj3-0 eGdfRW']/li[2]//strong")
    assert balance.text == "მობილური ბალანსის შევსება"
    balance.click()
    # check number input field and button
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='1213-abonentCode']")))
    chrome_driver.find_element_by_xpath("//*[@name='1213-abonentCode']").send_keys("593121314")
    chrome_driver.find_element_by_xpath("//*[@class='sc-1salb0b-1 laXiIz sc-9g6oqq-0 goRuDt']").click()
    # choose from select
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='select-input ']/label")))
    chrome_driver.find_element_by_xpath("//*[@class='select-input ']/label").click()
    assert chrome_driver.find_element_by_xpath("//*[@class='options']/a[2]/span").text == "ბალანსის შევსება"
    assert chrome_driver.find_element_by_xpath("//*[@class='options']/a[3]/span").text == '"მეტი" - 8 ₾'
    assert chrome_driver.find_element_by_xpath("//*[@class='options']/a[4]/span").text == '"მეტი" - 10 ₾'
    sleep(2)
    # press ten
    chrome_driver.find_element_by_xpath("//*[@class='options']/a[4]").click()
    # check assert
    sleep(3)
    chrome_driver.execute_script("window.scrollTo(0,document.body.scrollHeight/4)")
    el = chrome_driver.find_element_by_xpath("//*[@class='main-block sc-1ohd7xg-0 fybdwH']/div[1]/small/span")
    assert el.text == "დავალიანება"
    assert chrome_driver.find_element_by_xpath("//*[@class='debt']").text == "10.00 c"
    assert chrome_driver.find_element_by_xpath("//*[@class='debt']/span").text == "c"
    assert chrome_driver.find_element_by_xpath("//*[@class='main-block sc-1ohd7xg-0 fybdwH']/div[2]//span").text == "თანხის ოდენობა"
    assert chrome_driver.find_element_by_xpath("//*[@class='main-block sc-1ohd7xg-0 fybdwH']/div[2]//span[2]").text == "c"
    assert chrome_driver.find_element_by_xpath("//*[@class='readOnly']").get_attribute("value") == "10"
    assert chrome_driver.find_element_by_xpath(" //*[@class='commission-text sc-184o9l6-0 fEsIZw']//span").text == "საკომისიო"
    assert chrome_driver.find_element_by_xpath("//*[@class='commission-amount']//span").text == "0.12"
    assert chrome_driver.find_element_by_xpath("//*[@class='info']//span").text == "ჯამში გადასახდელი"
    assert chrome_driver.find_element_by_xpath("//*[@class='info']//b").text == "10.12 c"
    elem = chrome_driver.find_element_by_xpath("//button[@class='pay-btn sc-9g6oqq-0 goRuDt']")
    elem.click()
    sleep(5)
