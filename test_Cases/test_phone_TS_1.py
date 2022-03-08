import sys

import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_Cases.locators_phone import *

#import

driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, ph_product))).click()

assert wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/h2"))).text == "Samsung galaxy s6"

wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, ph_add_to_cart_btn))).click()

time.sleep(2)

alert = driver.switch_to.alert

print(alert.text)

alert.accept()

wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, cart_btn))).click()

p1 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//td[text()='Samsung galaxy s6']"))).text

#print(p1)

assert p1 == "Samsung galaxy s6"

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, place_order_btn))).click()

wait.until(expected_conditions.visibility_of_element_located((By.ID, name_txt_field))).send_keys("Akhil")
wait.until(expected_conditions.visibility_of_element_located((By.ID, country_txt_field))).send_keys("India")
wait.until(expected_conditions.visibility_of_element_located((By.ID, city_txt_field))).send_keys("Bangalore")
wait.until(expected_conditions.visibility_of_element_located((By.ID, card_txt_field))).send_keys("2345-9876")
wait.until(expected_conditions.visibility_of_element_located((By.ID, month_txt_field))).send_keys("March")
wait.until(expected_conditions.visibility_of_element_located((By.ID, year_txt_field))).send_keys("2022")

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, purchase_btn))).click()

time.sleep(2)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, confirmation_ok_btn))).click()

driver.quit()
