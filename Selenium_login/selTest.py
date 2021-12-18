from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('D:/Selenium_login/chromedriver.exe')


driver.get("http://127.0.0.1:3000/")
driver.maximize_window()
driver.find_element_by_name("email").send_keys("charitha@madala")
driver.find_element_by_name("username").send_keys("charitha")
driver.find_element_by_name("password").send_keys("1234")
driver.find_element_by_name("passwordConf").send_keys("1234")
driver.find_element_by_name("Register").click()

driver.find_element_by_name("email").send_keys("charitha@madala")
driver.find_element_by_name("password").send_keys("1234")