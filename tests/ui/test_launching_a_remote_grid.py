import pytest
from src.pages.login_page import LoginPage


@pytest.mark.usefixtures("get_driver_remote")
class TestLogin:
    def test_to_liteсart_online(self):
        self.remote_object = LoginPage(self.driver)
        self.remote_object.go_online()
        assert self.remote_object.at_page()
