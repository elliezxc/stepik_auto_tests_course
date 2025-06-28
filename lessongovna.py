from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим все обязательные поля (те, у которых есть символ * в label)
    required_labels = browser.find_elements(By.XPATH, "//label[contains(text(), '*')]")

    # Для каждого обязательного поля находим соответствующий input и заполняем
    for label in required_labels:
        input_id = label.get_attribute("for")
        if input_id:  # если у label есть атрибут for
            input_field = browser.find_element(By.ID, input_id)
        else:  # если нет, берем первый input после label
            input_field = label.find_element(By.XPATH, "./following-sibling::input[1]")
        input_field.send_keys("Тестовые данные")

    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем успешность регистрации
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()