import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from test_Cases.locators import *
from python_logic_seeker.test_Cases.locators import *
# from TestCase.locators import *
# from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_click))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_close))).click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_click))).click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_email))).send_keys("123@yopmail.com")
wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_name))).send_keys("shivanand")
wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_message))).send_keys(contact_message_text)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_send_message))).click()
driver.switch_to.alert.accept()

# login
login_click = wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, login_close))).click()

wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, login_username))).send_keys(account_text_username)
wait.until(expected_conditions.visibility_of_element_located((By.ID, login_password))).send_keys(account_text_password)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, account_login))).click()

driver.quit()
