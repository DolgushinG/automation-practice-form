from typing import Any

from selenium.webdriver.chrome.options import Options


def get_options(browser_name: str) -> Any:
    options = None
    if browser_name == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
    if browser_name == 'firefox':
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
    return options
