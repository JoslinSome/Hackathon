from selenium import webdriver
import os


print('__file__:    ', __file__)
PATH=os.getcwd()+"/chromedriver"
driver=webdriver.Chrome(PATH)
driver.get("https://www.techwithtim.net/")
