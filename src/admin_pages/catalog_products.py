import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.admin_pages.admin_page import AdminPageMenu


class AddNewProducts(AdminPageMenu):
    CATALOG_BTN = (By.XPATH, "//ul[@id='box-apps-menu']//*[contains(text(),'Catalog')]")
    STUDIO_FOLDER = (By.XPATH, "//table[@class='dataTable']//a[contains(text(), 'Studio')]")
    ADD_NEW_PRODUCT_BTN = (By.XPATH, "//*[contains(text(),'Add New Product')]")
    ENABLE_RADIO_BTN = "//input[@value='1']"
    PRODUCT_NAME_INPUT = (By.XPATH, "//input[@name='name[en]']")
    PRODUCT_CODE_INPUT = (By.XPATH, "//input[@name='code']")
    QUANTITY_PRODUCT = (By.XPATH, "//input[@name='quantity']")
    ADD_IMAGE = (By.XPATH, "//input[@name='new_images[]']")
    TAB_INFORMATION = (By.XPATH, "//ul[@class='index']/li/a[contains(text(),'Information')]")
    PRODUCT_KEYWORDS_INPUT = (By.XPATH, "//input[@name='keywords']")
    PRODUCT_SHORT_DESCRIPTION_INPUT = (By.XPATH, "//input[@name='short_description[en]']")
    PRODUCT_DESCRIPTION_EDITOR = (By.XPATH, "//div[@class='trumbowyg-editor']")
    PRODUCT_HEAD_TITLE_INPUT = (By.XPATH, "//input[@name='head_title[en]']")
    PRODUCT_META_DESCRIPTION_INPUT = (By.XPATH, "//input[@name='meta_description[en]']")
    TAB_PRICES = (By.XPATH, "//ul[@class='index']/li/a[contains(text(),'Prices')]")
    PRODUCT_PURCHASE_PRICE = (By.XPATH, "//input[@name='purchase_price']")
    PRODUCT_PRICE_USD = (By.XPATH, "//input[@name='prices[USD]']")
    SAVE_PRODUCT = (By.XPATH, "//button[@value='Save']")
    NEW_PRODUCT = (By.XPATH, "//table[@class='dataTable']//a[contains(text(),'red-kingston mouse')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step
    def add_new_product(self):
        self.driver.find_element(*self.CATALOG_BTN).click()
        self.driver.find_element(*self.STUDIO_FOLDER).click()
        self.driver.find_element(*self.ADD_NEW_PRODUCT_BTN).click()
        self.tab_general()

    @allure.step
    def tab_general(self):
        enable_radio_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ENABLE_RADIO_BTN)))
        if enable_radio_btn.is_displayed():
            enable_radio_btn.click()
        self.driver.find_element(*self.PRODUCT_NAME_INPUT).clear()
        self.driver.find_element(*self.PRODUCT_NAME_INPUT).send_keys("red-kingston mouse")
        self.driver.find_element(*self.PRODUCT_CODE_INPUT).clear()
        self.driver.find_element(*self.PRODUCT_CODE_INPUT).send_keys("010101")
        self.driver.find_element(*self.QUANTITY_PRODUCT).clear()
        self.driver.find_element(*self.QUANTITY_PRODUCT).send_keys('25')
        dir_image = '/home/oleg/Pictures/product/unnamed.png'
        self.driver.find_element(*self.ADD_IMAGE).send_keys(dir_image)
        self.tab_information()

    @allure.step
    def tab_information(self):
        self.driver.find_element(*self.TAB_INFORMATION).click()
        self.driver.find_element(*self.PRODUCT_KEYWORDS_INPUT).clear()
        self.driver.find_element(*self.PRODUCT_KEYWORDS_INPUT).send_keys("mouse")
        self.driver.find_element(*self.PRODUCT_SHORT_DESCRIPTION_INPUT).clear()
        self.driver.find_element(*self.PRODUCT_SHORT_DESCRIPTION_INPUT).send_keys("mouse for laptop")
        self.driver.find_element(*self.PRODUCT_DESCRIPTION_EDITOR).clear()
        description = """Mute quite clicks makes you concentrate on your work and free you worry about bothering others. 
        Powerful, reliable 2.4GHz wireless mouse connection with high anti-interference performance with 50ft/15M transmission distance.
        A Mini USB receiver (stored in the battery slot) supports plug and play."""
        description = ' '.join(description.split())
        self.driver.find_element(*self.PRODUCT_DESCRIPTION_EDITOR).send_keys(description)
        self.driver.find_element(*self.PRODUCT_HEAD_TITLE_INPUT).clear()
        self.driver.find_element(*self.PRODUCT_HEAD_TITLE_INPUT).send_keys("Kingstone")
        self.driver.find_element(*self.PRODUCT_META_DESCRIPTION_INPUT).clear()
        self.driver.find_element(*self.PRODUCT_META_DESCRIPTION_INPUT).send_keys("Mute quite clicks")
        self.tab_prices()

    @allure.step
    def tab_prices(self):
        self.driver.find_element(*self.TAB_PRICES).click()
        self.driver.find_element(*self.PRODUCT_PURCHASE_PRICE).clear()
        self.driver.find_element(*self.PRODUCT_PURCHASE_PRICE).send_keys("1.50")
        self.driver.find_element(*self.PRODUCT_PRICE_USD).clear()
        self.driver.find_element(*self.PRODUCT_PRICE_USD).send_keys("5.00")
        self.driver.find_element(*self.SAVE_PRODUCT).click()
        return self

    def check_added_product(self):
        self.driver.find_element(*self.CATALOG_BTN).click()
        self.driver.find_element(*self.STUDIO_FOLDER).click()
        self.driver.find_element(*self.NEW_PRODUCT).click()
        product_title = "Edit Product: red-kingston mouse | My Store"
        return product_title in self.driver.title
