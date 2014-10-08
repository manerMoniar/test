# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""

driver = webdriver.Firefox()
driver.get("http://mawd1tic.com/maw/")
elem = driver.find_element_by_css_selector("#content > div > div > div:nth-child(3) > div > div > div.span6.plain_text.alignment_left > h1")
assert elem.text == "Nuestros Servicios"
driver.close()