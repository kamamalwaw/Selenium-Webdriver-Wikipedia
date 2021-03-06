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
from wikipedia_city_page import WikipediaCityPage


class TestCityMajor():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')
    self.vars = {}
    self.driver.set_window_size(899, 1040)
  
  def teardown_method(self, method):
    self.driver.quit()


  def test_prezydent(self):

    #Arrange
    self.driver.get("https://pl.wikipedia.org/")

    #Act
    wikipedia_main_page = WikipediaMainPage(driver=self.driver)
    wikipedia_city_page = WikipediaCityPage(driver=self.driver)
    wikipedia_main_page.go_to_city("Gdynia")

    #Assert
    assert wikipedia_city_page.get_major_name() == "Wojciech Szczurek"


  def test_prezydent_1(self):

    #Arrange
    self.driver.get("https://pl.wikipedia.org/")

    #Act
    wikipedia_main_page = WikipediaMainPage(driver=self.driver)
    wikipedia_city_page = WikipediaCityPage(driver=self.driver)
    wikipedia_main_page.go_to_city("Gdańsk")

    #Assert
    assert wikipedia_city_page.get_major_name() == "Aleksandra Dulkiewicz"



  def test_prezydent_2(self):

    #Arrange
    self.driver.get("https://pl.wikipedia.org/")

    #Act
    wikipedia_main_page = WikipediaMainPage(driver=self.driver)
    wikipedia_city_page = WikipediaCityPage(driver=self.driver)
    wikipedia_main_page.go_to_city("Sopot")

    #Assert
    assert wikipedia_city_page.get_major_name() == "Jacek Karnowski"

  # def test_gdaskprezydent(self):
  #   self.driver.get("https://pl.wikipedia.org/")
  #   wikipedia_main_page = WikipediaMainPage(driver=self.driver)
  #   wikipedia_main_page.go_to_city("Gdańsk")
  #   assert self.driver.find_element(By.XPATH, "//table//node()[contains(text(), \"Prezydent\")]/ancestor::tr/td[2]").text == "Aleksandra Dulkiewicz"
