import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_Cases.home_footer_locators import *
from Logging.log_file import *

# from TestCase.locators import *
# from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 20)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Email validation
email_info = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, email))).text
assert email_info == email_details

# Phone number validation
phone_info = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, phone))).text
assert phone_info == phone_details

# Address
address_info = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, address))).text
assert address_info == address_Details
