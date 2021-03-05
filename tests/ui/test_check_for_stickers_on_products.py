import pytest
from src.pages.product_listing_page_objects import ProductsStickers


@pytest.mark.usefixtures('get_driver_remote_browser_stack')
class TestStickersProducts:
    def test_check_for_stickers(self):
        self.product_stickers = ProductsStickers(self.driver)
        self.product_stickers.go()
        assert self.product_stickers.check_stickers_on_products()

    def test_check_sticker_on_each_product(self):
        self.sticker_on_each_products = ProductsStickers(self.driver)
        self.sticker_on_each_products.go()
        assert self.sticker_on_each_products.each_product_exactly_has_one_stickers()
