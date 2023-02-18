
import json
import os
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import pyautogui
from typing import List, Optional
from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
import re
import yaml
from datetime import datetime, timedelta


log = logging.getLogger(__name__)

driver = webdriver.Chrome(ChromeDriverManager().install())


def setupLogger()->None:
    date_and_time = datetime.now().date()

    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(filename=('./logs/' + str(date_and_time)+ '.log'), filemode='w',
                        format='%(asctime)s::%(name)s::%(levelname)s::%(message)s', datefmt='./logs/%d-%b-%y %H:%M:%S')
    log.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)
    c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%H:%M:%S')
    c_handler.setFormatter(c_format)
    log.addHandler(c_handler)
    print("Logger setup complete")





class main():
    setupLogger()

    def __init__(self, username, password, phone):
        self.username = username
        self.password = password
        self.phone = phone
        self.options = self.browser_options()
        self.browser= driver
        self.wait = WebDriverWait(self.browser, 30)
        self.start(self.username, self.password)
        log.info("Welcome to linkedin bot")
        dirpath: str = os.getcwd()
        log.info("current directory is : " + dirpath)


    
    def browser_options(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")

        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return options


    def start(self,username,password)-> None:
        log.info("Logging in")
        self.browser.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
        try:
            user_field = self.browser.find_element("id","username")
            pw_field = self.browser.find_element("id","password")
            login_button = self.browser.find_element("xpath",
                        '//*[@id="organic-div"]/form/div[3]/button')
            user_field.send_keys(username)
            user_field.send_keys(Keys.TAB)
            time.sleep(2)
            pw_field.send_keys(password)
            time.sleep(2)
            login_button.click()
            time.sleep(3)
        except TimeoutException:
            log.info("TimeoutException! Username/password field or login button not found")
            
            

    def applyJobs(self):
        self.browser.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103644278&keywords=python%20developer&location=India")
    
    def get_easy_apply_button(self):
        try:
            easy_apply_button = self.browser.find_elements("xpath","//button[contains(@class,'jobs-apply-button')]")[0]
            return easy_apply_button
        except:
            return None


if __name__ == "__main__":
    with open('config.json','r') as stream:
        try:
            parameters = json.load(stream)
        except Exception as e:
            log.error(e)
            raise e
    assert parameters['username'] != None, "Username is not defined"
    assert parameters['password'] != None, "Password is not defined"
    assert parameters['phone'] != None, "Phone is not defined"
    main(parameters['username'], parameters['password'], parameters['phone'])


