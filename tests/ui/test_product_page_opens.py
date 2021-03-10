import pytest
from src.pages.product_page_opens import ProductPage


@pytest.mark.usefixtures('get_driver_chrome')
class TestProductPages:
    def test_correct_product_opens(self):
        first_product = ProductPage(self.driver)
        first_product.go()
        assert first_product.click_and_check_correct_product_page_opens()

    def test_comparison_names(self):
        first_product = ProductPage(self.driver)
        first_product.go()
        assert first_product.check_similarity_of_names()

    def test_comparison_price(self):
        first_product = ProductPage(self.driver)
        first_product.go()
        assert first_product.check_similarity_of_price()

    def test_comparison_css_property_of_price(self):
        first_product = ProductPage(self.driver)
        first_product.go()
        assert first_product.check_css_property_price_of_product()

