import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.admin_pages.countries_and_geozones import GeoZonesCountries


class CountriesEdit(GeoZonesCountries):
    UKRAINE = (By.XPATH, "//form[@name='countries_form']//*[contains(text(),'Ukraine')]")
    CODE_ALPHA_2 = (By.XPATH, "//input[@name='iso_code_2']/following-sibling::a")
    CODE_ALPHA_3 = (By.XPATH, "//input[@name='iso_code_3']/parent::td/a")
    TAX_ID_FORMAT = (By.XPATH, "//i[@class='fa fa-external-link']/parent::a[contains(@href, 'Regular')]")
    ADDRESS_FORMAT = (By.XPATH, "//i[@class='fa fa-external-link']/parent::a[contains(@href, 'address-formats')]")
    POSTCODE_FORMAT = (By.XPATH, "//input[contains(@name,'postcode_format')]/parent::td/a")
    CURRENCY_CODE = (By.XPATH, "//input[contains(@name,'currency_code')]/parent::td/a")
    PHONE_COUNTRY_CODE = (By.XPATH, "//input[contains(@name,'phone_code')]/parent::td/a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_countries_menu_item(self):
        self.driver.find_element(*self.LOCATOR_COUNTRIES_PAGE).click()

    def click_country_for_edit(self):
        self.driver.find_element(*self.UKRAINE).click()

    def window_processing(self, locator, main_window):
        quantity = len(self.driver.window_handles)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(quantity))
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

    def check_links(self):
        main_window = self.driver.current_window_handle

        locator_alpha_2 = self.driver.find_element(*self.CODE_ALPHA_2).click()
        self.window_processing(locator_alpha_2, main_window)
        alpha_2 = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)

        locator_alpha_3 = self.driver.find_element(*self.CODE_ALPHA_3).click()
        self.window_processing(locator_alpha_3, main_window)
        alpha_3 = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)

        locator_tax_id = self.driver.find_element(*self.TAX_ID_FORMAT).click()
        self.window_processing(locator_tax_id, main_window)
        tax_id_format = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)

        locator_address = self.driver.find_element(*self.ADDRESS_FORMAT).click()
        self.window_processing(locator_address, main_window)
        address_format = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)

        locator_postcode = self.driver.find_element(*self.POSTCODE_FORMAT).click()
        self.window_processing(locator_postcode, main_window)
        postcode_format = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)

        locator_currency_code = self.driver.find_element(*self.CURRENCY_CODE).click()
        self.window_processing(locator_currency_code, main_window)
        currency_code = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)

        locator_phone_code = self.driver.find_element(*self.PHONE_COUNTRY_CODE).click()
        self.window_processing(locator_phone_code, main_window)
        phone_country_code = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)

        return (alpha_2 == "ISO 3166-1 alpha-2 - Wikipedia" and alpha_3 == "ISO 3166-1 alpha-3 - Wikipedia"
                and tax_id_format == "Regular expression - Wikipedia"
                and address_format == "International Address Format Validator: Verify Mailing Formats | Informatica"
                and postcode_format == "Regular expression - Wikipedia"
                and currency_code == "List of countries and capitals with currency and language - Wikipedia"
                and phone_country_code == "List of country calling codes - Wikipedia")
