from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    log_form = (By.CSS_SELECTOR,"#login_form")
    reg_form = (By.CSS_SELECTOR,"#register_form")

