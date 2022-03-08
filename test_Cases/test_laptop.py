import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_Cases.locators import *
#from Logging.log_file import *

driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")

driver.maximize_window()


driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 10)

# Contact
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_click))).click()
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_close))).click()

#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_click))).click()
#wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_email))).send_keys("123@yopmail.com")
#wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_name))).send_keys("shivanand")
#wait.until(expected_conditions.visibility_of_element_located((By.ID, contact_message))).send_keys(contact_message_text)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, contact_send_message))).click()
#driver.switch_to.alert.accept()

# login
#login_click = wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, login_close))).click()

#wait.until(expected_conditions.visibility_of_element_located((By.ID, login_btn))).click()
#wait.until(expected_conditions.visibility_of_element_located((By.ID, login_username))).send_keys(account_text_username)
#wait.until(expected_conditions.visibility_of_element_located((By.ID, login_password))).send_keys(account_text_password)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, account_login))).click()
#time.sleep(2)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, laptops))).click()
time.sleep(2)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, sonyvaio))).click()
time.sleep(2)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, macbook))).click()
#time.sleep(2)
laptops_name = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, sony_laptop_name))).text
assert laptops_name == "Sony vaio i5"
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, addtocart))).click()
time.sleep(5)

alert = driver.switch_to.alert
alert.accept()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, home))).click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, laptops))).click()
time.sleep(2)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, macbook))).click()
time.sleep(2)
laptops_name1 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/h2"))).text
assert laptops_name1 == "MacBook air"

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/div[2]/div/a"))).click()

time.sleep(5)

alert = driver.switch_to.alert
alert.accept()
time.sleep(5)


wait.until(expected_conditions.visibility_of_element_located((By.XPATH, cart_btn))).click()

run = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//td[normalize-space()='Sony vaio i5']"))).text
assert run == "Sony vaio i5"
price1 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/tr/td[3]"))).text

#assert price == totalprice

test = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//td[normalize-space()='MacBook air']"))).text
assert test == "MacBook air"
price2 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/tr[2]/td[3]"))).text

totalprice = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='totalp']"))).text
# converted strings into int
value1 = int(price1)
value2 = int(price2)

value3 = value1 + value2
value4 = int(totalprice)

assert value3 == value4

time.sleep(2)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, delete_btn))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, placeorder_btn))).click()
time.sleep(2)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, name))).send_keys("Purushotam")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, country))).send_keys("India")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, city))).send_keys("Bangalore")

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, card))).send_keys("4242424242424242")

#time.sleep(2)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, month))).send_keys("April")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, year))).send_keys("2022")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, purchase_btn))).click()
time.sleep(2)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, okay_btn))).click()


#driver.quit()
