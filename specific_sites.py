from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver


def stream_pi_com(driver: WebDriver, width: int = None, height: int = None):
    """Get Stream-pi.com"""
    driver.get("https://stream-pi.com")
    if height != None and width != None:
        driver.set_window_rect(height=height, width=width)

    theme = driver.find_element("xpath", '//*[@id="streampi-navbar-nav"]/div/div/label[@for="theme-toggler"]')
    theme.click()
    sleep(1)
    msg = driver.find_element("xpath", '//*[@id="new-site-toast"]/div/div[2]/button[1]')
    msg.click()
    sleep(2)
    driver.get_screenshot_as_file("streampiwebsite.png")

def passwordgenerator_samtheq_com(driver: WebDriver, width: int = None, height: int = None):
    """Get passwordgenerator.samtheq.com"""
    driver.get("https://passwordgenerator.samtheq.com/")
    if height != None and width != None:
        driver.set_window_rect(height=height, width=width)
    
    sleep(2)
    driver.get_screenshot_as_file("passwordgenerator.png")