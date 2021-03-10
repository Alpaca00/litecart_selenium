import pytest
import allure
from src.pages.login_page import LoginPage


@pytest.mark.usefixtures('get_driver_remote_browser_stack')
class TestLogin:
    def test_login_to_liteсart_page_object(self):
        self.page_object = LoginPage(self.driver)
        self.page_object.go_online()
        assert self.page_object.at_page()

    def test_wrong_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.go_online()
        self.login_page.login_to_litecart()
        assert self.login_page.wait_for_text_to_appear == "You are now logged in as John Doe."

