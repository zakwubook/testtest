from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def check_credentials(username, password):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Переход на страницу входа
    driver.get('https://wubook.net/wauth/wauth/')
    
    # Явные ожидания для полей ввода
    wait = WebDriverWait(driver, 10)  # 10 секунд ожидания
    try:
        username_input = wait.until(EC.presence_of_element_located((By.ID, "wauth_user")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "wauth_password")))

        # Вводим логин и пароль
        username_input.send_keys(username)
        password_input.send_keys(password)
        
        # Нажимаем кнопку входа
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
        
        # Ждем загрузки страницы после входа
        wait.until(EC.presence_of_element_located((By.XPATH, "//body")))  # Замените на более специфичный селектор, если возможно

        # Проверяем, произошла ли ошибка аутентификации
        if "Authentication Failed" in driver.page_source:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()