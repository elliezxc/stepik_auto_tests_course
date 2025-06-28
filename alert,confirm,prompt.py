
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
# Alert
#alert = browser.switch_to.alert
#alert.accept()

#confirm
#confirm = browser.switch_to.alert
#confirm.accept() or confirm.dismiss()

#prompt
#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()


# URL страницы
url = "http://suninjuly.github.io/alert_accept.html"

try:
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get(url)

    # Нажатие кнопки Submit
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()
#нажатие подтверждения у всплывающего окна
    confirm = driver.switch_to.alert
    confirm.accept()

    # Получаем значение x
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажатие кнопки Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Даем время для визуальной проверки
    time.sleep(5)

finally:
    # Закрытие браузера
    driver.quit()