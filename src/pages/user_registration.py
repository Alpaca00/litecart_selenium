import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from src.pages.login_page import LoginPage


class UserRegistration(LoginPage):
    NEW_CUSTOMERS_BTN = (By.XPATH, "//div[@id = 'box-account-login']//a[contains(@href, 'create_account')]")
    FIRST_NAME_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='firstname']")
    LAST_NAME_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='lastname']")
    ADDRESS_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='address1']")
    POSTCODE_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='postcode']")
    CITY_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='city']")
    COUNTRY_SELECT = (By.XPATH, "//span[@class='select2-selection select2-selection--single']")
    _EMAIL_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='email']")
    PHONE_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='phone']")
    SUBSCRIBE_RADIO_BTN = (By.XPATH, "//form[@name='customer_form']//input[@name='newsletter']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='confirmed_password']")
    CAPTCHA_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='captcha']")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//form[@name='customer_form']//button[@name='create_account']")
    ACCEPT_COOKIES_BTN = (By.XPATH, "//div[@id='cookies-acceptance-wrapper']//button[@name='accept_cookies']")
    LOGOUT = (By.XPATH, "//div[@id='box-account']//a[@href='http://localhost/litecart/en/logout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def to_register(self):
        self.driver.find_element(*self.NEW_CUSTOMERS_BTN).click()
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys("Jane")
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys("Doe")
        self.driver.find_element(*self.ADDRESS_INPUT).clear()
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys("Pennsylvania Avenue NW")
        self.driver.find_element(*self.POSTCODE_INPUT).clear()
        self.driver.find_element(*self.POSTCODE_INPUT).send_keys("1600")
        self.driver.find_element(*self.CITY_INPUT).clear()
        self.driver.find_element(*self.CITY_INPUT).send_keys("Washington")
        country = Select(self.driver.find_element(*self.COUNTRY_SELECT))
        country.select_by_visible_text("United States")
        self.driver.find_element(*self._EMAIL_INPUT).clear()
        self.driver.find_element(*self._EMAIL_INPUT).send_keys('janedoe@gmail.com')
        self.driver.find_element(*self.PHONE_INPUT).clear()
        self.driver.find_element(*self.PHONE_INPUT).send_keys('911')
        self.driver.find_element(*self.SUBSCRIBE_RADIO_BTN).click()
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('qwerty')
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys('qwerty')
        self.driver.find_element(*self.ACCEPT_COOKIES_BTN).click()
        self.driver.find_element(*self.CAPTCHA_INPUT).clear()
        handling_captcha = input("CAPTCHA")
        self.driver.find_element(*self.CAPTCHA_INPUT).send_keys(handling_captcha)
        self.driver.find_element(*self.CREATE_ACCOUNT_BTN).click()
        self.driver.find_element(*self.LOGOUT).click()
        return self

    def login_to_account_and_exit(self):
        self.driver.find_element(*self.LOGIN_EMAIL_INPUT).clear()
        self.driver.find_element(*self.LOGIN_EMAIL_INPUT).send_keys("janedoe@gmail.com")
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys('qwerty')
        self.driver.find_element(*self.LOGIN_SUBMIT_BTN).click()
        self.driver.find_element(*self.LOGOUT).click()
        return self
