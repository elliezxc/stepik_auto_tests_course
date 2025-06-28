import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://stepik.org/lesson/25969/step/12")
wait = WebDriverWait(driver, 10)

# 🔹 Нажимаем на кнопку "Войти"
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login")))
login_button.click()

# 🔹 Вводим email
email_input = wait.until(EC.presence_of_element_located((By.ID, "id_login_email")))
email_input.send_keys("lizkamail577@gmail.com")

# 🔹 Вводим пароль
password_input = driver.find_element(By.ID, "id_login_password")
password_input.send_keys("Kakashki555")

# 🔹 Нажимаем кнопку "Войти"
submit_login = driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
submit_login.click()

# 🔹 Ждём авторизации и загрузки страницы
time.sleep(5)

# 🔹 Обновляем страницу с уроком после входа
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# 🔹 Вводим ответ
textarea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
textarea.send_keys("get()")
time.sleep(2)

# 🔹 Закрываем возможное всплывающее сообщение
try:
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "woof-message__text")))
except:
    print("Всплывающее сообщение не исчезло, продолжаем...")

# 🔹 Кликаем по кнопке отправки
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()

# 🔹 Ждём немного и закрываем браузер
time.sleep(5)
driver.quit()

