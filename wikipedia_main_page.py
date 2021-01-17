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

class WikipediaMainPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_city(self, city_name):

        self.driver.find_element(By.ID, "searchInput").click()
        self.driver.find_element(By.ID, "searchInput").send_keys(city_name)
        self.driver.find_element(By.ID, "searchInput").send_keys(Keys.ENTER)

