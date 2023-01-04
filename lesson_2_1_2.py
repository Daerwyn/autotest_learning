from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    value = driver.find_element(By.CSS_SELECTOR, "#treasure").get_attribute('valuex')
    y = calc(value)
    ans = driver.find_element(By.CSS_SELECTOR, '# answer')
    ans.send_keys(y)
    chk = driver.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    chk.click()
    rrl = driver.find_element(By.CSS_SELECTOR, '#robotsRule')
    rrl.click()
    subm = driver.find_element(By.XPATH, "//button[text()='Submit']")
    subm.click()


finally:
    time.sleep(10)
    driver.quit()
