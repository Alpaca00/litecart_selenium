import pytest
import allure
from src.pages.check_for_stickers_on_products import ProductsStickers


@pytest.mark.usefixtures('get_driver_chrome')
class TestStickersProducts:
    @allure.title("availability of stickers")
    def test_check_for_stickers(self):
        self.product_stickers = ProductsStickers(self.driver)
        self.product_stickers.go()
        with allure.step("Check availability of stickers"):
            assert self.product_stickers.check_stickers_on_products()

    def test_check_sticker_on_each_product(self):
        self.sticker_on_each_products = ProductsStickers(self.driver)
        self.sticker_on_each_products.go()
        with allure.step("each product exactly has one stickers"):
            assert self.sticker_on_each_products.each_product_exactly_has_one_stickers()
