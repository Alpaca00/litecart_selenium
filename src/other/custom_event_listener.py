from datetime import datetime
import time
import csv
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init
from colorama import Fore, Back
from pyvirtualdisplay import Display


init(autoreset=True)


class CustomEventListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):

        print(Fore.BLACK + Back.RED + f"Before navigating to {url}")
        print(Fore.BLACK + Back.GREEN + f"Current url before navigating to {url} is '{driver.current_url}'")
        print(Fore.BLACK + Back.GREEN + f"Page title before navigating to {url} is '{driver.title}'\n")

    def after_navigate_to(self, url, driver):

        print(Fore.BLACK + Back.RED + f"After navigating to {url}")
        print(Fore.BLACK + Back.GREEN + f"Current url after navigating to {url} is '{driver.current_url}'")
        print(Fore.BLACK + Back.GREEN + f"Page title after navigating to {url} is '{driver.title}'\n")

    def before_find(self, by, value, driver):

        print(Fore.BLACK + Back.RED + f"Searching for element with '{by}={value}' on {driver.current_url}\n")

    def after_find(self, by, value, driver):

        print(Fore.BLACK + Back.GREEN + f"Found element with '{by}={value}' on {driver.current_url}\n")

    def on_exception(self, exception, driver):
        print(exception)

    def before_quit(self, driver):

        print(Fore.BLACK + Back.RED + f"Quitting the browser with url: {driver.current_url}")
        print(Fore.BLACK + Back.RED + "Bye ...\n")

    def after_quit(self, driver):

        print(Fore.BLACK + Back.GREEN + "Quit a browser!")


class LoginPageEventListener:
    driver = None
    display = Display(visible=0, size=(1920, 2160))

    def __init__(self, driver):
        self.driver = driver
        self.event_listener = CustomEventListener()
        self.event_firing_driver = EventFiringWebDriver(driver, self.event_listener)
        self.display.start()

    def go(self):
        self.event_firing_driver.get("http://localhost/litecart/en/")

    def login_to_an_existing_account(self):
        self.event_firing_driver.find_element_by_xpath("//input[@name='email']").clear()
        self.event_firing_driver.find_element_by_xpath("//input[@name='email']").send_keys("johndoe@gmail.com")
        self.event_firing_driver.find_element_by_xpath("//input[@name='password']").clear()
        self.event_firing_driver.find_element_by_xpath("//input[@name='password']").send_keys("1qaz2wsx3edc")
        self.event_firing_driver.find_element_by_xpath("//button[@type='submit']").click()

    def get_log(self):
        current_time = datetime.now().strftime("%d_%m_%y")
        with open(f"/home/oleg/python/litecart_local/doc/log_date_{current_time}.txt", "w") as log_file:
            writer = csv.writer(log_file)
            log = self.driver.get_log("browser")
            print(log)
            writer.writerow(log)

    def get_screenshot(self):
        filename = f"/home/oleg/python/litecart_local/doc/{self.driver.title}.png"
        time.sleep(1)
        self.driver.save_screenshot(filename)

    def quit(self):
        time.sleep(1)
        self.display.stop()
        self.event_firing_driver.quit()


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,2160")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    john = LoginPageEventListener(driver)
    john.go()
    john.login_to_an_existing_account()
    john.get_log()
    john.get_screenshot()
    john.quit()


if __name__ == '__main__':
    main()
