import pytest
from src.admin_pages.check_logs_on_admin_page_for_product_catalog import LogsProductCatalog


@pytest.mark.usefixtures("get_driver_chrome")
class TestProductsOnCatalogs:
    def test_presence_of_logs(self):
        self.product_pages = LogsProductCatalog(self.driver)
        self.product_pages.home_page.go()
        self.product_pages.home_page.login_to_admin_page()
        self.product_pages.open_catalog_of_products()
        self.product_pages.computer_engineering_open_catalog()
        self.product_pages.check_logs_for_all_products()
        assert self.product_pages.check_all_event_by_pages(16)
