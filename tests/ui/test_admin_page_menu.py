import pytest
from src.admin_pages.admin_page import AdminPageMenu


@pytest.mark.usefixtures('get_driver_chrome')
class TestAdminMenu:
    def test_admin_login(self):
        self.admin_login = AdminPageMenu(self.driver)
        self.admin_login.go()
        self.admin_login.login_to_admin_page()
        self.admin_login.get_logs()
        assert self.admin_login.at_main_page()

    def test_clicks_all_menu_items_including_nested(self):
        self.admin_menu = AdminPageMenu(self.driver)
        self.admin_menu.go()
        self.admin_menu.login_to_admin_page()
        self.admin_menu.clicks_all_menu_items()
        assert self.admin_menu.quantity_titles_at_pages(48)



