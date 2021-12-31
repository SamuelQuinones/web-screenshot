from selenium.webdriver import Chrome, Firefox, Edge

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOps
from selenium.webdriver.firefox.options import Options as FireFoxOps
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.edge.options import Options as EdgeOps
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class BrowserHelper:
    def __init__(self, browser: str = "chrome", arguments: list[str] = ["--headless"]) -> None:
        self.browser = browser
        self.arguments = set(arguments)
    
    def add_argument(self, argument):
        self.arguments.add(argument)

    def use_chrome(self):
        """
        Tell the class to use the Google Chrome browser
        """
        my_service = ChromeService(executable_path=ChromeDriverManager().install())

        my_opts = ChromeOps()
        for opt in self.arguments:
            my_opts.add_argument(opt)

        driver = Chrome(service=my_service, options=my_opts)
        return driver

    def use_firefox(self):
        """
        Tell the class to use the Firefox browser
        """
        my_service = FireFoxService(executable_path=GeckoDriverManager().install())

        my_opts = FireFoxOps()
        for opt in self.arguments:
            my_opts.add_argument(opt)
    
        driver = Firefox(service=my_service, options=my_opts)
        return driver

    def use_edge(self):
        """
        Tell the class to use the Chromium Edge browser
        """
        my_service = EdgeService(executable_path=EdgeChromiumDriverManager(log_level=20).install())

        my_opts = EdgeOps()
        for opt in self.arguments:
            my_opts.add_argument(opt)
        
        driver = Edge(service=my_service, options=my_opts)
        return driver


    def auto(self):
        if self.browser == "chrome":
            return self.use_chrome()
        elif self.browser == "firefox":
            return self.use_firefox()
        elif self.browser == "edge":
            return self.use_edge()
        else:
            raise Exception("Acceptable Browser Not Found")
