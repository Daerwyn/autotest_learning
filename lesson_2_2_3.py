from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'requirements.txt')

try:
    driver.get(link)
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    file = driver.find_element(By.CSS_SELECTOR, "input#file")
    first_name.send_keys('Koko')
    last_name.send_keys('Okok')
    email.send_keys('koko@okok.ko')
    file.send_keys(file_path)
    subm = driver.find_element(By.XPATH, "//button[text()='Submit']")
    subm.click()

finally:
    time.sleep(5)
    driver.quit()