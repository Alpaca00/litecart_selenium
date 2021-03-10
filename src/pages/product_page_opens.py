import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.login_page import LoginPage
import time


class ProductPage(LoginPage):
    CAMPAIGNS_FIRST_PRODUCT = (By.XPATH, "//div[@id='box-campaigns']//a[contains(@href, 'sony-monitor-p-12')]")
    MAIN_PAGE_PRODUCT_NAME = (By.XPATH, "//div[@id='box-campaigns']//a[@title='Sony Monitor']/div[contains(text(),'Sony Monitor')]")
    MAIN_PAGE_OLD_PRICE_FIRST_PRODUCT = (By.XPATH, "//div[@id='box-campaigns']//a[contains(@href, 'sony-monitor-p-12')]//s[@class='regular-price']")
    MAIN_PAGE_NEW_PRICE_FIRST_PRODUCT = (By.XPATH, "//div[@id='box-campaigns']//a[contains(@href, 'sony-monitor-p-12')]//strong[@class='campaign-price']")
    PRODUCT_ON_PAGE = (By.XPATH, "//div[@id='box-product']//h1[contains(text(), 'Sony Monitor')]")
    PRODUCT_OLD_PRICE_ON_PAGE = (By.XPATH, "//div[@id='box-product']//s[@class ='regular-price']")
    PRODUCT_NEW_PRICE_ON_PAGE = (By.XPATH, "//div[@id='box-product']//strong[@class ='campaign-price']")
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_and_check_correct_product_page_opens(self):
        self.driver.find_element(*self.CAMPAIGNS_FIRST_PRODUCT).click()
        time.sleep(3)
        title = self.driver.title
        must_be_title = "Sony Monitor | Studio | My Store"
        return title == must_be_title

    def check_similarity_of_names(self):
        main_page_product_name = self.driver.find_element(*self.MAIN_PAGE_PRODUCT_NAME).text
        self.driver.find_element(*self.CAMPAIGNS_FIRST_PRODUCT).click()
        product_name_on_page = self.driver.find_element(*self.PRODUCT_ON_PAGE).text
        return main_page_product_name == product_name_on_page

    def check_similarity_of_price(self):
        main_page_old_price = self.driver.find_element(*self.MAIN_PAGE_OLD_PRICE_FIRST_PRODUCT).text
        main_page_new_price = self.driver.find_element(*self.MAIN_PAGE_NEW_PRICE_FIRST_PRODUCT).text
        self.driver.find_element(*self.CAMPAIGNS_FIRST_PRODUCT).click()
        product_old_price_on_page = self.driver.find_element(*self.PRODUCT_OLD_PRICE_ON_PAGE).text
        product_new_price_on_page = self.driver.find_element(*self.PRODUCT_NEW_PRICE_ON_PAGE).text
        return main_page_old_price == product_old_price_on_page and main_page_new_price == product_new_price_on_page

    def check_css_property_price_of_product(self):
        main_page_old_price_css_style = self.driver.find_element(*self.MAIN_PAGE_OLD_PRICE_FIRST_PRODUCT)
        main_page_new_price_css_style = self.driver.find_element(*self.MAIN_PAGE_NEW_PRICE_FIRST_PRODUCT)

        color_old_price = main_page_old_price_css_style.value_of_css_property("color") #rgba(119, 119, 119, 1)
        color_new_price = main_page_new_price_css_style.value_of_css_property("color") #rgba(204, 0, 0, 1)

        font_size_old = main_page_old_price_css_style.value_of_css_property("font-size") #14.4px
        font_size_new = main_page_new_price_css_style.value_of_css_property("font-size") #18px

        font_weight_old = main_page_old_price_css_style.value_of_css_property("font-weight") #400
        font_weight_new = main_page_new_price_css_style.value_of_css_property("font-weight") #700

        self.driver.find_element(*self.CAMPAIGNS_FIRST_PRODUCT).click()
        on_page_old_price_css_style = self.driver.find_element(*self.PRODUCT_OLD_PRICE_ON_PAGE)
        on_page_new_price_css_style = self.driver.find_element(*self.PRODUCT_NEW_PRICE_ON_PAGE)

        on_page_color_old_price = on_page_old_price_css_style.value_of_css_property("color") #rgba(102, 102, 102, 1)
        on_page_color_new_price = on_page_new_price_css_style.value_of_css_property("color") #rgba(204, 0, 0, 1)

        on_page_font_size_old = on_page_old_price_css_style.value_of_css_property("font-size") #16px
        on_page_font_size_new = on_page_new_price_css_style.value_of_css_property("font-size") #22px

        on_page_font_weight_old = on_page_old_price_css_style.value_of_css_property("font-weight") #400
        on_page_font_weight_new = on_page_new_price_css_style.value_of_css_property("font-weight") #700

        return (color_new_price == on_page_color_new_price
                and font_weight_new == on_page_font_weight_new
                and font_size_new and on_page_font_size_new == "18px" or "22px"
                and color_old_price and on_page_color_old_price == "rgba(119, 119, 119, 1)" or "rgba(102, 102, 102, 1)"
                and font_size_old and on_page_font_size_old == "14.4px" or "16px"
                and font_weight_old == on_page_font_weight_old)



