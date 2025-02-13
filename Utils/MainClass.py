from http.server import executable

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class MainClass:

    def __init__(self, browser, type_of_screen):
        self.driver = None
        self.select_browser(browser)
        self.select_mode(type_of_screen)
        print('Test execution started in ' + browser + ' browser ' + type_of_screen + ' mode')

    def select_browser(self, browser):
        if browser == 'Chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(options=options)
        elif browser == "Firefox":
            browser_options = webdriver.FirefoxOptions()
            browser_options.headless = True
            browser_options.add_argument("--ignore-certificate-errors")
            service = Service(executable_path='../drivers/geckodriver.exe')
            self.driver = webdriver.Firefox(service=service, options=browser_options)
        elif browser == "Edge":
            browser_options = webdriver.EdgeOptions()
            browser_options.headless = True
            browser_options.add_argument("--ignore-certificate-errors")
            service = Service(executable_path='../drivers/msedgedriver.exe')
            self.driver = webdriver.Edge(service=service, options=browser_options)

    def select_mode(self, type_of_screen):
        if type_of_screen == 'full_screen':
            self.driver.maximize_window()
        elif type_of_screen == 'mobile_screen':
            self.driver.set_window_size(390, 840)

    def open_url(self, base_url):
        print('Opening the url - ' + base_url)
        self.driver.get(base_url)

    @staticmethod
    def get_element_type(locator_type):
        if locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'xpath':
            return  By.XPATH
        elif locator_type == 'id':
            return  By.ID
        elif locator_type == 'class_name':
            return  By.CLASS_NAME
        elif locator_type == 'tag_name':
            return  By.TAG_NAME

    def get_element(self, locator, locator_type):
        return self.driver.find_element(self.get_element_type(locator_type), locator)

    def get_elements(self, loc):
        return self.driver.find_elements(self.get_element_type(loc.get_locator_type()), loc.get_locator())

    def type_text(self, loc, text):
        print('Typing ' + text + ' in ' + loc.get_locator_name() + ' element')
        try:
            self.get_element(loc.get_locator(), loc.get_locator_type()).send_keys(text)
        except:
            raise Exception("Unable to type in " + loc.get_locator_name())

    def click_element(self, loc):
        print('Clicking ' + loc.get_locator_name() + ' element')
        try:
            self.get_element(loc.get_locator(), loc.get_locator_type()).click()
        except:
            raise Exception("Unable to click the " + loc.get_locator_name())

    def get_text(self, loc):
        return self.get_element(loc.get_locator(), loc.get_locator_type()).text

    def clear_element(self, loc):
        print('Clearing ' + loc.get_locator_name() + ' element')
        self.get_element(loc.get_locator(), loc.get_locator_type()).clear()

    def is_visible(self, loc):
        element = self.get_element(loc.get_locator(), loc.get_locator_type())
        if element.is_displayed():
            print(loc.get_locator_name() + ' is displayed')
        else:
            raise Exception(loc.get_locator_name() + ' is not displayed')

    def scroll_to_element(self, loc):
        print('Scrolling to ' + loc.get_locator_name() + ' element')
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element(loc.get_locator(), loc.get_locator_type())).perform()

    def select_from_dropdown(self, loc, element_to_be_selected):
        print('Selecting '+ element_to_be_selected + ' from ' + loc.get_locator_name() + ' dropdown menu')
        sel = Select(self.get_element(loc.get_locator(), loc.get_locator_type()))
        sel.select_by_visible_text(element_to_be_selected)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def wait_seconds(self, time):
        self.driver.implicitly_wait(time)

    def wait_until_element_is_present(self, loc):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located
                   ((self.get_element_type(loc.get_locator_type()), loc.get_locator())))

    def quit_driver(self):
        self.driver.quit()
        print('Test execution completed')
