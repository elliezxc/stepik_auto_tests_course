import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Путь к файлу
file_path = "/Users/ellie/Downloads/imya.txt"

# URL страницы
url = "https://suninjuly.github.io/file_input.html"

try:
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get(url)

    # Заполнение текстовых полей
    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys("Имя")

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("Фамилия")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("test@example.com")

    # Загрузка файла
    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Проверка существования файла
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")

    # Нажатие кнопки Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Даем время для визуальной проверки
    time.sleep(5)

finally:
    # Закрытие браузера
    driver.quit()