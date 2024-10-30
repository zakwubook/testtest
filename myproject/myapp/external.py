from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

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
        
        # Ждем, пока URL изменится
        wait.until(EC.url_changes(driver.current_url))

        # Проверяем, на какую страницу мы перенаправлены
        if driver.current_url == "https://wubook.net/zks/manage/dboard/":
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()
