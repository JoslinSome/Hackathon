import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = os.getcwd() + "/chromedriver"


class webScrape:

    reqs_list = []

    def __init__(self):
        self.driver = webdriver.Chrome(PATH, options=options)
        self.driver.get("https://catalog.registrar.uiowa.edu/your-program/")
        webScrape.reqs_list = []

    def search_major(self, program):
        no_errors = False
        try:
            buttons = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), '{},')]".format(program)))).click()
            no_errors = True
        except:
            return False
        if no_errors:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//a[text()="Requirements"]'))).click()
            requirements_button = self.driver.find_element_by_id("requirementstexttab")
            requirements_button.click()
            course_odd = self.driver.find_elements_by_class_name('odd')
            for course in course_odd:
                try:
                    course_info = course.text
                    if len(course_info.split()) != 0 and "these" not in course_info:
                        webScrape.reqs_list.append(course_info)
                except:
                    pass
            course_even = self.driver.find_elements_by_class_name("even")
            for course1 in course_even:
                try:
                    course_info1 = course1.text
                    if len(course_info1.split()) != 0 and "these" not in course_info1:
                        webScrape.reqs_list.append(course_info1)
                except:
                    pass

            return True