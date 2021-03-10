import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.pages.login_page import LoginPage


class UserRegistration(LoginPage):
    NEW_CUSTOMERS_BTN = (By.XPATH, "//div[@id = 'box-account-login']//a[contains(@href, 'create_account')]")
    FIRST_NAME_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='firstname']")
    LAST_NAME_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='lastname']")
    ADDRESS_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='address1']")
    POSTCODE_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='postcode']")
    CITY_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='city']")
    COUNTRY_SELECT = (By.XPATH, "//select[@name='country_code']")
    ZONE_SELECT = (By.XPATH, "//select[@name='zone_code']")
    EMAIL_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='email']")
    PHONE_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='phone']")
    SUBSCRIBE_RADIO_BTN = (By.XPATH, "//form[@name='customer_form']//input[@name='newsletter']")
    PASSWORD_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='confirmed_password']")
    CAPTCHA_INPUT = (By.XPATH, "//form[@name='customer_form']//input[@name='captcha']")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//form[@name='customer_form']//button[@name='create_account']")
    ACCEPT_COOKIES_BTN = (By.XPATH, "//div[@id='cookies-acceptance-wrapper']//button[@name='accept_cookies']")
    LOGOUT = (By.XPATH, "//div[@id='box-account']//a[contains(@href,'logout')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def to_register_and_logout_after_re_login_and_logout(self):
        self.driver.find_element(*self.NEW_CUSTOMERS_BTN).click()
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys("Jane")
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys("Doe")
        self.driver.find_element(*self.ADDRESS_INPUT).clear()
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys("Pennsylvania Avenue NW")
        self.driver.find_element(*self.POSTCODE_INPUT).clear()
        self.driver.find_element(*self.POSTCODE_INPUT).send_keys("20001")
        self.driver.find_element(*self.CITY_INPUT).clear()
        self.driver.find_element(*self.CITY_INPUT).send_keys("Washington")
        country = Select(self.driver.find_element(*self.COUNTRY_SELECT))
        country.select_by_visible_text("United States")
        zone = Select(self.driver.find_element(*self.ZONE_SELECT))
        zone.select_by_visible_text("Washington")
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys('jane1@gmail.com')
        self.driver.find_element(*self.PHONE_INPUT).clear()
        self.driver.find_element(*self.PHONE_INPUT).send_keys('+101101')
        self.driver.find_element(*self.SUBSCRIBE_RADIO_BTN).click()
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('qwertyas')
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys('qwertyas')
        self.driver.find_element(*self.ACCEPT_COOKIES_BTN).click()
        self.driver.find_element(*self.CAPTCHA_INPUT).clear()
        handling_captcha = "0000" # file: create_account.inc.php - I changed if captcha != post input!!!
        self.driver.find_element(*self.CAPTCHA_INPUT).send_keys(handling_captcha)
        self.driver.find_element(*self.CREATE_ACCOUNT_BTN).click()
        try:
            profile_logout_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@id='box-account']//a[contains(@href,'logout')]")))
            if profile_logout_element.is_displayed():
                profile_logout_element.click()
        except TimeoutException:
            return False
        self.driver.find_element(*self.LOGIN_EMAIL_INPUT).clear()
        self.driver.find_element(*self.LOGIN_EMAIL_INPUT).send_keys("jane1@gmail.com")
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys('qwertyas')
        self.driver.find_element(*self.LOGIN_SUBMIT_BTN).click()
        self.driver.find_element(*self.LOGOUT).click()
        return self


