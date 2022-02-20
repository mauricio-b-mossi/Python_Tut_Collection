from selenium import webdriver
# abilitates keyboard keys
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# open
driver.get("https://www.techwithtim.net/")
search = driver.find_element_by_name('s')
search.send_keys("test")
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(5)