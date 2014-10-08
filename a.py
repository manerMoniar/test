from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lettuce_webdriver.webdriver  

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
driver.get("http://127.0.0.1:5000/appointments/")
elem = driver.find_element_by_css_selector("#main > div.content.container > div > div:nth-child(1) > div > h3 > a")
assert elem.text == "Past Meeting"
driver.close()