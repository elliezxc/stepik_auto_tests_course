from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.ID, "num1")
    x1 = int(x1_element.text)
    x2_element = browser.find_element(By.ID, "num2")
    x2 = int(x2_element.text)
    y = str(x1 + x2)


    # Находим выпадающий список и выбираем значение по value
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()