import pytest
from src.pages.user_registration import UserRegistration


@pytest.mark.usefixtures("get_driver_chrome")
class TestUserRegistration:
    def test_user_registration(self):
        first_person = UserRegistration(self.driver)
        first_person.go()
        assert first_person.to_register_and_logout_after_re_login_and_logout()
