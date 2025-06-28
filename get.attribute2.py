from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент-картинку с id="treasure"
    treasure = browser.find_element(By.ID, "treasure")

    # Получаем значение атрибута "valuex"
    x = treasure.get_attribute("valuex")

    # Вычисляем значение по формуле
    y = calc(x)

    # Вводим результат в поле
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Отмечаем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()