
import pytest
from selenium import webdriver
#from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Browser drivers\Chrome v.98\chromedriver_win32 (2)\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.demoblaze.com/index.html")

