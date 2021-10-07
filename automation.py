from selenium import webdriver
from selenium.webdriver.common.keys import Keys

file_username = open("username.txt","r")
file_pass = open("pass.txt","r")
user_name = file_username.read()
password = file_pass.read()

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

fb = driver.find_element_by_id("email")
fb.send_keys(user_name)

fb = driver.find_element_by_id("pass")
fb.send_keys(password)

fb.send_keys(Keys.RETURN)