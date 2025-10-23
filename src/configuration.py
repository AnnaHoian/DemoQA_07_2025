import configparser
import os
from pathlib import Path


class Configuration:

    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.parser.read(Path(os.getenv('CONFIG_PATH', 'config.ini')).absolute())

    def get_browser(self):
        """ Get Selenium instance of driver (Chrome, FF, etc.)"""
        # TODO DEMO-QA-003 Implement getting selenium driver in configuration class
        pass

    def get_base_url(self):
        return self.parser.get('demoqa', 'url')

CONFIG = Configuration()