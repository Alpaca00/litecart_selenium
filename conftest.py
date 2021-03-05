import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from doc2.browser_stack import BROWSERSTACK_URL, desired_cap


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


@pytest.fixture(scope="function")
def get_driver_remote_kvm_win7(request):
    driver = webdriver.Remote("http://192.168.122.1:4444/wd/hub", desired_capabilities={"browserName": "internet explorer"})
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def get_driver_remote_browser_stack(request):
    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def get_driver_remote_inside_containers(request):
    driver = webdriver.Remote("http://192.168.122.1:4444/wd/hub", desired_capabilities={"browserName": "chrome"})
    request.cls.driver = driver
    yield
    driver.quit()
