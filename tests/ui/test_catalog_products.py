import pytest
from src.admin_pages.catalog_products import AddNewProducts


@pytest.mark.usefixtures("get_driver_chrome")
class TestAddProduct:
    def test_add_product(self):
        new_product = AddNewProducts(self.driver)
        new_product.go()
        new_product.login_to_admin_page()
        new_product.add_new_product()

    def test_check_product_added(self):
        created_product = AddNewProducts(self.driver)
        created_product.go()
        created_product.login_to_admin_page()
        assert created_product.check_added_product()
