import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from wikipedia_main_page import WikipediaMainPage

class WikipediaCityPage:

    def __init__(self, driver):
        self.driver = driver

    def get_major_name(self) -> str:
    # z assercji w City Major
       return self.driver.find_element(By.XPATH,"//table//node()[contains(text(), 'Prezydent')]/ancestor::tr/td[2]").text