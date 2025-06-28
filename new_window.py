from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем кнопку, которая откроет новое окно с задачей
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    # Переключаемся на новое окно (индекс 1, так как индекс 0 - это исходное окно)
    browser.switch_to.window(browser.window_handles[1])

    # Решаем задачу во втором окне
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отправляем решение
    submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
