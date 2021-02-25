import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartProducts:
    PRODUCT_LAPTOP = (By.XPATH, "//div[@id='box-campaigns']//li/a[@title='Laptop']")
    ADD_TO_CART = (By.XPATH, "//button[contains(text(), 'Add To Cart')]")
    PRODUCTS_COUNTER_OF_CART = "//div[@id='cart']/a/span[@class='quantity']"
    CHECKOUT_BTN = (By.XPATH, "//div[@id='cart']/a[contains(text(), 'Checkout')]")
    UPDATE_QUANTITY_INPUT = (By.XPATH, "//form[@name='cart_form']//input[@name='quantity']")
    UPDATE_BTN = (By.XPATH, "//button[@name='update_cart_item']")
    UPDATE_TABLE = "//div[@id='order_confirmation-wrapper']//tr[2]/td[1]"
    CLEAR_CART = "//*[contains(text(),'no items')]"

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get("http://localhost/litecart/en/")

    def click_product_and_add_a_few_to_cart(self):
        for item in range(1, 4):
            self.driver.find_element(*self.PRODUCT_LAPTOP).click()
            self.driver.find_element(*self.ADD_TO_CART).click()
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, self.PRODUCTS_COUNTER_OF_CART), str(item)))
            self.driver.back()

    def open_cart(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def delete_one_by_one_and_wait_for_table_to_updates(self):
        update = self.driver.find_element(*self.UPDATE_QUANTITY_INPUT)
        self.driver.execute_script("arguments[0].value= '2';", update)
        self.driver.find_element(*self.UPDATE_BTN).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, self.UPDATE_TABLE), "2"))
        next_update = self.driver.find_element(*self.UPDATE_QUANTITY_INPUT)
        self.driver.execute_script("arguments[0].value= '1';", next_update)
        self.driver.find_element(*self.UPDATE_BTN).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, self.UPDATE_TABLE), "1"))
        last_update = self.driver.find_element(*self.UPDATE_QUANTITY_INPUT)
        self.driver.execute_script("arguments[0].value= '0';", last_update)
        self.driver.find_element(*self.UPDATE_BTN).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, self.CLEAR_CART), "There are no items in your cart."))
        empty_cart = self.driver.find_element_by_xpath(self.CLEAR_CART).text
        return empty_cart == "There are no items in your cart."
