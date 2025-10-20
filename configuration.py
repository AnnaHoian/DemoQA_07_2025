import configparser
import os


class Configuration:

    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.parser.read(os.getenv('CONFIG_PATH', 'config.ini'))

    def get_browser(self):
        """ Get Selenium instance of driver (Chrome, FF, etc.)"""
        # TODO DEMO-QA-003 Implement getting selenium driver in configuration class
        pass