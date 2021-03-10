import pytest
import allure
from src.pages.user_registration import UserRegistration


@pytest.mark.usefixtures("get_driver_remote_inside_containers")
class TestUserRegistration:
    @allure.title("User Registration")
    def test_user_registration(self):
        first_person = UserRegistration(self.driver)
        first_person.go()
        with allure.step("to register and logout after re login and logout"):
            assert first_person.to_register_and_logout_after_re_login_and_logout()
