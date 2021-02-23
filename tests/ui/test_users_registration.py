import pytest
from src.pages.user_registration import UserRegistration


@pytest.mark.usefixtures("get_driver_chrome")
class TestUserRegistration:
    def test_user_registration(self):
        first_person = UserRegistration(self.driver)
        first_person.go()
        assert first_person.to_register()

    def test_user_login_to_account(self):
        first_person = UserRegistration(self.driver)
        first_person.go()
        assert first_person.login_to_account_and_exit()
