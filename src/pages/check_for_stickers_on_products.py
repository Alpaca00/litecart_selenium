import allure
from selenium.webdriver.common.by import By


class OutAttributeError(Exception):
    def __init__(self, txt, attribute):
        self.txt = txt
        self.attribute = attribute

    def __str__(self):
        return f"{self.txt}/n{self.attribute}"


class ProductsStickers:
    GROUP_MOST_POPULAR = (By.XPATH, "//div[contains(@id, 'box-most-popular')]//ul[@class='listing-wrapper products']/li")
    GROUP_LATEST_PRODUCTS = (By.XPATH, "//div[contains(@id, 'box-latest-products')]//ul[@class='listing-wrapper products']/li")
    GROUP_CAMPAINGS_PRODUCTS = (By.XPATH, "//div[contains(@id, 'box-campaigns')]//ul[@class='listing-wrapper products']/li")
    GROUP_STICKERS_PRODUCTS = (By.XPATH, "//*[@class='sticker new' or @class='sticker sale']")
    LST_PRODUCTS = []
    LST_STICKERS = []
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def go(self):
        self.driver.get("http://localhost/litecart/en/")

    def are_elements_present(self, *args):
        return len(*args) > 0

    def check_stickers_on_products(self):
        group_most_popular = self.driver.find_elements(*self.GROUP_MOST_POPULAR)
        group_latest_product = self.driver.find_elements(*self.GROUP_LATEST_PRODUCTS)
        group_campaings_product = self.driver.find_elements(*self.GROUP_CAMPAINGS_PRODUCTS)
        group_stickers_products = self.driver.find_elements(*self.GROUP_STICKERS_PRODUCTS)
        if self.are_elements_present(group_most_popular) and self.are_elements_present(group_latest_product)\
                and self.are_elements_present(group_campaings_product):
            for item in range(0, len(group_most_popular)):
                group_most_popular = self.driver.find_elements(*self.GROUP_MOST_POPULAR)
                self.LST_PRODUCTS.append(group_most_popular[item].text)
            for item in range(0, len(group_latest_product)):
                group_latest_product = self.driver.find_elements(*self.GROUP_LATEST_PRODUCTS)
                self.LST_PRODUCTS.append(group_latest_product[item].text)
            for item in range(0, len(group_campaings_product)):
                group_campaings_product = self.driver.find_elements(*self.GROUP_CAMPAINGS_PRODUCTS)
                self.LST_PRODUCTS.append(group_campaings_product[item].text)
        if self.are_elements_present(group_stickers_products):
            for item in range(0, len(group_stickers_products)):
                group_stickers_products = self.driver.find_elements(*self.GROUP_STICKERS_PRODUCTS)
                self.LST_STICKERS.append(group_stickers_products[item].text)
        return len(self.LST_PRODUCTS) == len(self.LST_STICKERS)

    def each_product_exactly_has_one_stickers(self):
        self.check_stickers_on_products()
        group = self.driver.find_elements(*self.GROUP_STICKERS_PRODUCTS)
        if self.are_elements_present(group):
            for item in range(0, len(group)):
                group = self.driver.find_elements(*self.GROUP_STICKERS_PRODUCTS)
                attribute = group[item].get_attribute("title")
                try:
                    if attribute == "New↵Sale":
                        raise OutAttributeError("Value for attribute ->", attribute)
                except OutAttributeError as err:
                    print(f"Extra attribute for element: {err}")
            return self

