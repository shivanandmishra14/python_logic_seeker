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

login_click = wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, login_close))).click()

# wrong credentials
# wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
# wait.until(expected_conditions.visibility_of_element_located((By.ID, login_username))).send_keys(wrong_cred_username)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, login_password))).send_keys(wrong_cred_password)
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, account_login))).click()
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, login_close))).click()
#
# time.sleep(2)
# driver.switch_to.alert.accept()
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, wrong_cred_close))).click()

# Login
wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, login_username))).send_keys(account_text_username)
wait.until(expected_conditions.visibility_of_element_located((By.ID, login_password))).send_keys(account_text_password)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, account_login))).click()

# username
verify_logged_in_username = wait.until(
    expected_conditions.visibility_of_element_located((By.XPATH, logged_in_username))).text
assert verify_logged_in_username == logged_in_user_name_text
