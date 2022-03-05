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

driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 20)

wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, login_close))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, home_btn))).click()

driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, home_next))).click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, home_previous))).click()
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

# banner
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, home_banner_forward_btn)))
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, home_banner_backward_btn)))



