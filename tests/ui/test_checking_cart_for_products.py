import pytest
from src.pages.cart_for_products import CartProducts


@pytest.mark.usefixtures("get_driver_chrome")
class TestCartProduct:
    def test_add_a_few_products_to_cart_and_all_delete(self):
        product = CartProducts(self.driver)
        product.go()
        product.click_product_and_add_a_few_to_cart()
        product.open_cart()
        assert product.delete_one_by_one_and_wait_for_table_to_updates()
