import pytest
import allure
from src.admin_pages.admin_page import AdminPageMenu


@pytest.mark.usefixtures('get_driver_chrome')
class TestAdminMenu:
    @allure.title("Login into admin page")
    def test_admin_login(self):
        self.admin_login = AdminPageMenu(self.driver)
        self.admin_login.go()
        self.admin_login.login_to_admin_page()
        self.admin_login.check_logs()
        with allure.step("at_main_page"):
            assert self.admin_login.at_main_page()

    @allure.title("Clicks all items of menu")
    def test_clicks_all_menu_items_including_nested(self):
        self.admin_menu = AdminPageMenu(self.driver)
        self.admin_menu.go()
        self.admin_menu.login_to_admin_page()
        self.admin_menu.clicks_all_menu_items()
        with allure.step("quantity_titles_at_pages"):
            assert self.admin_menu.quantity_titles_at_pages(48)



