from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .app import App


class Selper():
    """
    This class is a helper class to separate our selenium specific code. 
    Don't write any kind of custom logic here in this class. It's for your own good. :D 
    """

    __driver = None

    def __init__(self):
        self.__configure()

    def prepare(self):
        """
        Prepares a new instance for the driver.
        """

        # start chrome browser with options to consume less amount of resource and on server environment this is the best option
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('user-agent={}'.format(App.user_agent()))
        # chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("window-size=1366,768")

        # enables the capturing of the console logs from the browser
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        caps['goog:loggingPrefs'] = {'browser': 'ALL'}

        if(App.is_prod()):
            self.__driver = webdriver.Chrome(
                executable_path=App.driver_path(), options=chrome_options, desired_capabilities=caps)
            print("selenium driver prepared for PROD", flush=True)
        else:
            co = Options()
            co.add_argument("window-size=1366,768")
            self.__driver = webdriver.Chrome(
                executable_path=App.driver_path(), options=co, desired_capabilities=caps)
            print("selenium driver prepared for DEV", flush=True)

    def __configure(self):
        self.prepare()

    def driver(self):
        return self.__driver

    def exec_javascript(self, code):
        self.__driver.execute_script(code)
