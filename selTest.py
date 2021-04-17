import os
from selenium import webdriver
PATH=os.getcwd()+"/chromedriver"
driver=webdriver.Chrome(PATH)
driver.get("https://catalog.registrar.uiowa.edu/your-program/")
# if ("Accounting" in driver.page_source):
#      # text exists in page
#     print("Yes")
# else:
#     print("No")
buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Accounting')]")

for btn in buttons:
    btn.click()