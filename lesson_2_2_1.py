from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects2.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    num_1 = driver.find_element(By.CSS_SELECTOR, '#num1.nowrap')
    num_2 = driver.find_element(By.CSS_SELECTOR, '#num2.nowrap')
    num_3 = int(num_1.text) + int(num_2.text)
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(num_3))
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    driver.quit()