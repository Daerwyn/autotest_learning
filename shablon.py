from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
driver = webdriver.Chrome()

try:
    driver.get(link)

finally:
    time.sleep(5)
    driver.quit()