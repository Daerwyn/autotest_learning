from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    first.send_keys('Asdf')
    second = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    second.send_keys('Asdfas')
    third = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    third.send_keys('Asdfas')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
