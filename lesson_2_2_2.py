from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    value = driver.find_element(By.XPATH, "//span[@id='input_value']")
    x = value.text
    y = calc(x)
    ans = driver.find_element(By.CSS_SELECTOR, '#answer')
    ans.send_keys(y)
    subm = driver.find_element(By.XPATH, "//button[text()='Submit']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", subm)
    chk = driver.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    chk.click()
    rrl = driver.find_element(By.CSS_SELECTOR, '#robotsRule')
    rrl.click()
    subm.click()


finally:
    time.sleep(5)
    driver.quit()
