from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
 link = "https://suninjuly.github.io/selects1.html"
 browser = webdriver.Chrome()
 browser.get(link)
 x = browser.find_element(By.ID, 'num1').text
 y = browser.find_element(By.ID, 'num2').text
 select = Select(browser.find_element(By.TAG_NAME, "select"))
 select.select_by_value(str(int(x)+int(y)))
 submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
 time.sleep(10)

finally:
 browser.quit()


