import pytest
from src.admin_pages.links_on_country_edit_page_open_in_new_window import CountriesEdit


@pytest.mark.usefixtures("get_driver_chrome")
class TestCheckLinks:
    def test_open_for_editing_and_check_links(self):
        country = CountriesEdit(self.driver)
        country.go()
        country.login_to_admin_page()
        country.click_countries_menu_item()
        country.click_country_for_edit()
        assert country.check_links()
