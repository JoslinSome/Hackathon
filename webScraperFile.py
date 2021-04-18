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
PATH = os.getcwd() + "/chromedriver.exe"


class webScrape:

    reqs_list = []

    def __init__(self):
        self.driver = webdriver.Chrome(PATH, options=options)
        # self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://catalog.registrar.uiowa.edu/your-program/")
        webScrape.reqs_list = []

    def search_major(self, program):
        # search_bar = self.driver.find_element_by_id("quicksearch")
        # search_bar.clear()
        # search_bar.send_keys(program)
        # search_bar.send_keys(Keys.RETURN)
        # program_name = self.driver.find_element_by_class_name("filterimage")
        # span_name = program_name.find_element_by_tag_name("span")
        # for x in span_name:
            # print("Hi")
        # except:
            # print("This program does not exist, please enter another")
        no_errors = False
        try:
            buttons = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), '{},')]".format(program)))).click()
            no_errors = True
        except:
            return False
        if no_errors:
            # for btn in buttons:
                # btn.click()
                # break
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//a[text()="Requirements"]'))).click()
            requirements_button = self.driver.find_element_by_id("requirementstexttab")
            requirements_button.click()
            # course_list = self.driver.find_element_by_class_name("sc_courselist")
            course_odd = self.driver.find_elements_by_class_name('odd')
            for course in course_odd:
                try:
                    course_info = course.text
                    if len(course_info.split()) != 0 and "these" not in course_info:
                        print(course_info)
                        webScrape.reqs_list.append(course_info)
                except:
                    pass
            course_even = self.driver.find_elements_by_class_name("even")
            for course1 in course_even:
                try:
                    course_info1 = course1.text
                    if len(course_info1.split()) != 0 and "these" not in course_info1:
                        print(course_info1)
                        webScrape.reqs_list.append(course_info1)
                except:
                    pass
            # print(self.driver.title)
            check_answer = False
            while not check_answer:
                user_input = input("Enter 0 to quit: ")
                if user_input == "0":
                    check_answer = True
                    self.driver.close()
                    print("Hello")


start_program = webScrape()
# user_input1 = input("Enter Major: ")
user_input1 = "Accounting"
program_runs = start_program.search_major(user_input1)
if not program_runs:
    print("Could not find major, please re-enter")
