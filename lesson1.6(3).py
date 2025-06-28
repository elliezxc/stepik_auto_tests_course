from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все текстовые поля формы с помощью CSS-селектора
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    # Заполняем каждое поле текстом "Мой ответ"
    for element in elements:
        element.send_keys("Мой ответ")

    # Находим и кликаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла