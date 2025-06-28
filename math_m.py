from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем radiobutton
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Отправляем форму
    submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
