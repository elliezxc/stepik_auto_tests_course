from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/get_attribute.html")

treasure = browser.find_element(By.ID, "treasure")
x = treasure.get_attribute("valuex")  # получаем значение скрытого атрибута
print(x)
