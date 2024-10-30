from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def check_credentials(username, password):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Вводим логин и пароль
    username_input = driver.find_element(By.ID, "wauth_user")
    password_input = driver.find_element(By.ID, "wauth_password")
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    # Нажимаем кнопку входа
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    time.sleep(2)  # Ждем загрузки страницы

    if "Authentication Failed" not in driver.page_source:
        driver.get('https://wubook.net/zks/manage/dboard/')
        time.sleep(2)  # Ждем загрузки страницы
        if '<input class="uk-input" id="zak_team_username" autocomplete="new-password">' in driver.page_source:
            driver.quit()
            return False
        else:
            driver.quit()
            return True

    driver.quit()
    return False