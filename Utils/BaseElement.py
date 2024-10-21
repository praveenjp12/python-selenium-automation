from selenium import webdriver

class BaseElement:

    def __init__(self, locator_type, locator, locator_name):
        self.locator_type = locator_type
        self.locator = locator
        self.locator_name = locator_name


    def get_locator(self):
        return self.locator

    def get_locator_type(self):
        return self.locator_type

    def get_locator_name(self):
        return self.locator_name
