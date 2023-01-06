from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def test_registration(link):
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    first.send_keys('Asdf')
    second = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    second.send_keys('Asdfas')
    third = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    third.send_keys('Asdfas')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(5)
    browser.quit()


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        test_registration(link)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        test_registration(link)


if __name__ == '__main__':
    unittest.main()
