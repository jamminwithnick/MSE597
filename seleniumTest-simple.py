import os.path
from os import path
from selenium import webdriver

selenium_grid_url = "http://localhost:4444/wd/hub"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_argument("--start-maximized")

driverlocation = "C:\\Users\\SW-VnV6\\Downloads\\chromedriver.exe"

driver = webdriver.Chrome(driverlocation,options = chromeOptions, desired_capabilities = chromeOptions.to_capabilities())
driver.get("http://www.google.com")
item=driver.find_element_by_xpath("//*[@id=\"hplogo\"]/a/img")
item.click()

