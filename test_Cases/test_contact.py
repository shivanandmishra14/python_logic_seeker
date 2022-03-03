import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_Cases.locators import *
from Logging.log_file import *

# from TestCase.locators import *
# from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 20)

# Contact
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_click))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_close))).click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_click))).click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_email))).send_keys("123@yopmail.com")
wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_name))).send_keys("shivanand")
wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_message))).send_keys(contact_message_text)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_send_message))).click()
driver.switch_to.alert.accept()

# driver.quit()
