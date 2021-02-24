import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def get_driver_chrome(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def get_driver_firefox(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    yield
    driver.quit()
