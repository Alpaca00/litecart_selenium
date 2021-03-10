import pytest
import allure
from src.admin_pages.check_links_on_country_page import CountriesEdit


@pytest.mark.usefixtures("get_driver_chrome")
class TestCheckLinks:
    @allure.title("Check all links")
    def test_open_country_and_check_links(self):
        country = CountriesEdit(self.driver)
        country.go()
        country.login_to_admin_page()
        country.click_countries_menu_item()
        country.click_country_for_edit()
        with allure.step("All links are directed to Wikipedia"):
            assert country.check_links()
