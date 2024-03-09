from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class BrowserWrapper:
    def __init__(self, browser_name):
        self.driver = self.initialize_driver(browser_name)

    def initialize_driver(self):
        if self.browser_name.lower() == "chrome":
            options = ChromeOptions()
            options.add_argument("--enable-logging")
            options.add_argument("--v=1")
        elif self.browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
        elif self.browser_name.lower() == "edge":
            options = EdgeOptions()

        else:
            raise ValueError("Unsupported browser")

        if self.config["grid"]:
            self.driver = webdriver.Remote(
                command_executor=self.config["hub_url"],
                options=options
            )
        else:
            if self.browser_name.lower() == "chrome":
                self.driver = webdriver.Chrome(options=options)
            elif self.browser_name.lower() == "firefox":
                self.driver = webdriver.Firefox(options=options)
            elif self.browser_name.lower() == "edge":
                self.driver = webdriver.Edge(options=options)

        self.driver.get(self.config["url"])
        return self.driver