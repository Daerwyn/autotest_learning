from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link)
    want_join = driver.find_element(By.CSS_SELECTOR, "button.trollface.btn")
    want_join.click()
    first_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
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
