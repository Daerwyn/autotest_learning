from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver.get(link)
    wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100"))
    book = driver.find_element(By.CSS_SELECTOR, "button#book")
    book.click()
    value = driver.find_element(By.XPATH, "//span[@id='input_value']")
    x = value.text
    y = calc(x)
    ans = driver.find_element(By.CSS_SELECTOR, '#answer')
    ans.send_keys(y)
    subm = driver.find_element(By.XPATH, "//button[text()='Submit']")
    subm.click()



finally:
    time.sleep(5)
    driver.quit()