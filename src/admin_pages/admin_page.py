import allure
from datetime import datetime
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common import alert


class AdminPageMenu:
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    GROUP_BOX_BTN = (By.XPATH, "//ul[@id='box-apps-menu']/li")
    SUB_GROUP_BTN = (By.XPATH, "//ul[@id='box-apps-menu']/li//li")
    QUANTITY_TITLES = []
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get("http://admin:admin@localhost/litecart/admin/")

    def login_to_admin_page(self):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('admin')
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def at_main_page(self):
        tls = "My Store"
        return tls in self.driver.title

    def check_logs(self):
        current_time = datetime.now().strftime("%d_%m_%y")
        with open(f"/home/oleg/python/litecart_local/doc/log_date_{current_time}.txt", "a") as log_file:
            writer = csv.writer(log_file)
            log = self.driver.get_log("browser")
            writer.writerow(log)

    def are_elements_present(self, *args):
        return len(*args) > 0

    def clicks_all_menu_items(self):
        group_catalog = self.driver.find_elements(*self.GROUP_BOX_BTN)
        if self.are_elements_present(group_catalog):
            for i in range(0, len(group_catalog)):
                group_catalog = self.driver.find_elements(*self.GROUP_BOX_BTN)
                group_catalog[i].click()
                title_text = self.driver.title
                self.QUANTITY_TITLES.append(title_text)
                sub_group_catalog = self.driver.find_elements(*self.SUB_GROUP_BTN)
                if self.are_elements_present(sub_group_catalog):
                    for item in range(1, len(sub_group_catalog)):
                        sub_group_catalog = self.driver.find_elements(*self.SUB_GROUP_BTN)
                        sub_group_catalog[item].click()
                        title_text = self.driver.title
                        self.QUANTITY_TITLES.append(title_text)

    def quantity_titles_at_pages(self, quantity: int):
        return len(self.QUANTITY_TITLES) == quantity



