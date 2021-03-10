import allure
from selenium.webdriver.common.by import By
from .admin_page import AdminPageMenu
from src.other.reader import read_logs

count = 0


class LogsProductCatalog:
    CATALOG_BTN = (By.XPATH, "//ul[@id='box-apps-menu']//*[contains(text(),'Catalog')]")
    COMPUTER_ENGINEERING = (By.XPATH, "//*[contains(text(),'Computer Engineering')]")
    GROUP_PRODUCTS = (By.XPATH, "//form[@name='catalog_form']//a[contains(@href, 'http') and not (contains(@title, 'Edit'))]")
    SALES = (By.XPATH, "//*[contains(text(),'Sales')]")
    STUDIO = (By.XPATH, "//*[contains(text(),'Studio')]")

    def __init__(self, driver):
        self.driver = driver
        self.home_page = AdminPageMenu(self.driver)

    @allure.step
    def open_catalog_of_products(self):
        self.driver.find_element(*self.CATALOG_BTN).click()
        self.home_page.check_logs()

    @allure.step
    def computer_engineering_open_catalog(self):
        global count
        self.driver.find_element(*self.COMPUTER_ENGINEERING).click()
        self.home_page.check_logs()
        group = self.driver.find_elements(*self.GROUP_PRODUCTS)
        for i in range(2, len(group)-2):
            count += 1
            group = self.driver.find_elements(*self.GROUP_PRODUCTS)
            group[i].click()
            self.home_page.check_logs()
            self.driver.back()
        self.sales_open_catalog()
        return self

    @allure.step
    def sales_open_catalog(self):
        global count
        self.driver.find_element(*self.SALES).click()
        self.home_page.check_logs()
        group = self.driver.find_elements(*self.GROUP_PRODUCTS)
        for i in range(3, len(group)-1):
            count += 1
            group = self.driver.find_elements(*self.GROUP_PRODUCTS)
            group[i].click()
            self.home_page.check_logs()
            self.driver.back()
        self.studio_open_catalog()
        return self

    @allure.step
    def studio_open_catalog(self):
        global count
        self.driver.find_element(*self.STUDIO).click()
        self.home_page.check_logs()
        group = self.driver.find_elements(*self.GROUP_PRODUCTS)
        for i in range(4, len(group)):
            count += 1
            group = self.driver.find_elements(*self.GROUP_PRODUCTS)
            group[i].click()
            self.home_page.check_logs()
            self.driver.back()
        return self

    @staticmethod
    def check_logs_for_all_products():
        return read_logs()

    def check_all_event_by_pages(self, event: int):
        global count
        return count == event



