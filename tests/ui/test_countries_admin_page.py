import pytest
from src.admin_pages.countries_and_geozones import GeoZonesCountries


@pytest.mark.usefixtures('get_driver_chrome')
class TestCountriesGeoZones:
    def test_check_list_countries(self):
        countries = GeoZonesCountries(self.driver)
        countries.go()
        countries.login_to_admin_page()
        assert countries.check_alphabetical_sequence_of_countries_in_list()

    def test_check_countries_geo_zones_list(self):
        countries_geo_zones = GeoZonesCountries(self.driver)
        countries_geo_zones.go()
        countries_geo_zones.login_to_admin_page()
        assert countries_geo_zones.check_alphabetical_sequence_of_countries_in_geo_zones_list()

    def test_check_geo_zones(self):
        geo_zones = GeoZonesCountries(self.driver)
        geo_zones.go()
        geo_zones.login_to_admin_page()
        assert geo_zones.check_alphabetical_sequence_in_geo_zones_page()
