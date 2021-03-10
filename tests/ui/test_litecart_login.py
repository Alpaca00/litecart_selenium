import pytest
import allure
from src.pages.login_page import LoginPage


@pytest.mark.usefixtures('get_driver_chrome')
class TestLogin:
    def test_login_to_liteсart_page(self):
        self.page_object = LoginPage(self.driver)
        self.page_object.go()
        with allure.step("At page"):
            assert self.page_object.at_page()

    def test_login_correct(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.go()
        self.login_page.login_to_litecart()
        with allure.step("Only logging in to the account"):
            assert self.login_page.wait_for_text_to_appear == "You are now logged in as John Doe."

