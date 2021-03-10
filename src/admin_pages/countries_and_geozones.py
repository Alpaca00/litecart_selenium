import copy
import allure
from selenium.webdriver.common.by import By
from src.admin_pages.admin_page import AdminPageMenu


class GeoZonesCountries(AdminPageMenu):
    LOCATOR_COUNTRIES_PAGE = (By.XPATH, "//ul[@id='box-apps-menu']//span[contains(text(), 'Countries')]")
    COUNTRIES_NAME = (By.XPATH, "//form[@name='countries_form']//td[5]/a")
    COUNTRIES_GEO_ZONES_QUANTITY = (By.XPATH, "//form[@name='countries_form']//td[6]")
    COUNTRIES_GEO_ZONES_SEQUENCE_OF_NAMES = (By.XPATH, "//table[@id='table-zones']//td[3]")
    BTN_SAVE_GEO_ZONES = (By.XPATH, "//button[@value='Save']")
    LST_SEQUENCE_NAMES_OF_COUNTRIES = []
    LST_SEQUENCE_NAMES_OF_GEO_ZONES = []
    LOCATOR_GEO_ZONES_PAGE = (By.XPATH, "//ul[@id='box-apps-menu']//span[contains(text(), 'Geo Zones')]")
    GEO_ZONES_EDIT_BTN = (By.XPATH, "//form[@name='geo_zones_form']//td[5]")
    LOCATOR_LST_SELECT_GEO_ZONES = (By.XPATH, "//table[@id='table-zones']//td[3]")
    LST_SEQUENCE_OF_GEO_ZONES_PAGE = []
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step
    def check_alphabetical_sequence_of_countries_in_list(self):
        self.driver.find_element(*self.LOCATOR_COUNTRIES_PAGE).click()
        group_countries_name = self.driver.find_elements(*self.COUNTRIES_NAME)
        for item in range(len(group_countries_name)):
            group_countries_name = self.driver.find_elements(*self.COUNTRIES_NAME)
            self.LST_SEQUENCE_NAMES_OF_COUNTRIES.append(group_countries_name[item].text)
        deep_copy_lst_sequence_names_of_countries = copy.deepcopy(self.LST_SEQUENCE_NAMES_OF_COUNTRIES)
        deep_copy_lst_sequence_names_of_countries.sort()
        return self.LST_SEQUENCE_NAMES_OF_COUNTRIES == deep_copy_lst_sequence_names_of_countries

    @allure.step
    def check_alphabetical_sequence_of_countries_in_geo_zones_list(self):
        self.driver.find_element(*self.LOCATOR_COUNTRIES_PAGE).click()
        group_geo_zones = self.driver.find_elements(*self.COUNTRIES_GEO_ZONES_QUANTITY)
        for item in range(1, len(group_geo_zones)):
            group_geo_zones = self.driver.find_elements(*self.COUNTRIES_GEO_ZONES_QUANTITY)
            geo_zones = group_geo_zones[item].text
            btn_item = f"(//form[@name='countries_form']//td[7]/a[@title='Edit'])[position()={item+1}]"
            if geo_zones != "0":
                self.driver.find_element_by_xpath(btn_item).click()
                geo_zones_sequence_of_names = self.driver.find_elements(*self.COUNTRIES_GEO_ZONES_SEQUENCE_OF_NAMES)
                for n in range(1, len(geo_zones_sequence_of_names)-1):
                    geo_zones_sequence_of_names = self.driver.find_elements(*self.COUNTRIES_GEO_ZONES_SEQUENCE_OF_NAMES)
                    self.LST_SEQUENCE_NAMES_OF_GEO_ZONES.append(geo_zones_sequence_of_names[n].text)
                self.driver.find_element(*self.BTN_SAVE_GEO_ZONES).click()
                deep_copy_lst_sequence_names_of_geo_zones = copy.deepcopy(self.LST_SEQUENCE_NAMES_OF_GEO_ZONES)
                deep_copy_lst_sequence_names_of_geo_zones.sort()
                assert self.LST_SEQUENCE_NAMES_OF_GEO_ZONES == deep_copy_lst_sequence_names_of_geo_zones
            self.LST_SEQUENCE_NAMES_OF_GEO_ZONES.clear()
        return self

    @allure.step
    def check_alphabetical_sequence_in_geo_zones_page(self):
        self.driver.find_element(*self.LOCATOR_GEO_ZONES_PAGE).click()
        group_edit_geo_zones = self.driver.find_elements(*self.GEO_ZONES_EDIT_BTN)
        for item in range(0, len(group_edit_geo_zones)):
            group_edit_geo_zones = self.driver.find_elements(*self.GEO_ZONES_EDIT_BTN)
            group_edit_geo_zones[item].click()
            group_zone = self.driver.find_elements(*self.LOCATOR_LST_SELECT_GEO_ZONES)
            for n in range(1, len(group_zone)+1):
                all_zone_locator = f"(//table[@id='table-zones']//td[3]/select/option[@selected])[position()={n}]"
                value = self.driver.find_element_by_xpath(all_zone_locator)
                self.LST_SEQUENCE_OF_GEO_ZONES_PAGE.append(value.text)
            deep_copy_lst_sequence_of_geo_zones_page = copy.deepcopy(self.LST_SEQUENCE_OF_GEO_ZONES_PAGE)
            deep_copy_lst_sequence_of_geo_zones_page.sort()
            self.driver.find_element(*self.BTN_SAVE_GEO_ZONES).click()
            assert self.LST_SEQUENCE_OF_GEO_ZONES_PAGE == deep_copy_lst_sequence_of_geo_zones_page
            deep_copy_lst_sequence_of_geo_zones_page = None
            self.LST_SEQUENCE_OF_GEO_ZONES_PAGE.clear()
        return self








