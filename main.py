
import os
import logging
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
    date_and_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(filename=('./logs/' + str(date_and_time) + 'applyJobs.log'), filemode='w',
                        format='%(asctime)s::%(name)s::%(levelname)s::%(message)s', datefmt='./logs/%d-%b-%y %H:%M:%S')
    log.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)
    c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%H:%M:%S')
    c_handler.setFormatter(c_format)
    log.addHandler(c_handler)
    print("Logger setup complete")





def main():
    setupLogger()


if __name__ == "__main__":
    main()


