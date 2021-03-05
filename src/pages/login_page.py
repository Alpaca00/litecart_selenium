import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get("http://192.168.122.1/litecart/en/")

    def go_online(self):
        self.driver.get("https://litecart.stqa.ru/en/")

    def login_to_litecart(self):
        self.driver.find_element(*self.LOGIN_EMAIL_INPUT).clear()
        self.driver.find_element(*self.LOGIN_EMAIL_INPUT).send_keys('johndoe@gmail.com')
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys('1qaz2wsx3edc')
        self.driver.find_element(*self.LOGIN_SUBMIT_BTN).click()

    def at_page(self):
        return "Online Store | My Store" in self.driver.title

    @property
    def wait_for_text_to_appear(self):
        self.driver.execute_script("document.getElementById('notices-wrapper').style='display: true;'")
        self.driver.implicitly_wait(5)
        return self.driver.find_element_by_xpath("//*[contains(text(), 'You are now logged in as John Doe.')]").text
