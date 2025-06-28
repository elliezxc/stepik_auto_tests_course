from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
button.click()

assert "successful" in message.text

#на вызов ошибки
#NoSuchElementException - нет такого вообще
#StaleElementReferenceException -  мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение
#ElementNotVisibleException - Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры)