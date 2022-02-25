import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_Cases.locators import *

driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 20)

wait.until(expected_conditions.visibility_of_element_located((By.ID, signup_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, signup_close))).click()

wait.until(expected_conditions.visibility_of_element_located((By.ID, signup_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, signup_username))).send_keys(signup_text_username)
wait.until(expected_conditions.visibility_of_element_located((By.ID, signup_password))).send_keys(signup_text_username)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, signup_account))).click()

time.sleep(2)
driver.switch_to.alert.accept()
