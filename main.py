import os
from helpers import BrowserHelper
from specific_sites import passwordgenerator_samtheq_com, stream_pi_com


if __name__ == "__main__":
    os.environ['WDM_LOCAL'] = '1'

    MY_BROWSER = BrowserHelper(browser="chrome", arguments=["--headless", "--hide-scrollbars"])

    driver = MY_BROWSER.auto()
    stream_pi_com(driver, 1280, 720)
    passwordgenerator_samtheq_com(driver, 1280, 720)
    driver.quit()