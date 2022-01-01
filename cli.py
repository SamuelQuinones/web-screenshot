import argparse
import os
from time import sleep
from helpers import BrowserHelper

my_parser = argparse.ArgumentParser(description='Grab screenshots of websites', allow_abbrev=False)

my_parser.add_argument('url', type=str, help="url to scrape")
my_parser.add_argument('--browser', '-b', type=str, help='choice of browser to use for scraping', choices=['chrome', 'edge', 'firefox'], default='chrome', metavar='')
my_parser.add_argument('--use-local', '-lo', help='use / download local browser driver', action='store_true', default=False)
my_parser.add_argument('--width', '-wi', type=int, help="width in pixels for the inner window", metavar='')
my_parser.add_argument('--height', '-he', type=int, help="height in pixels for the inner window", metavar='')
my_parser.add_argument('--browser-args', type=str, help="options to pass to the browser driver", metavar='', nargs='+', default=['headless'])
my_parser.add_argument('--wait', type=int, help='time to delay before screenshot is taken', metavar='', default=1)

def parse_browser_args(args):
    my_list = []
    for arg in args:
        my_list.append(f"--{arg}")
    
    return my_list


if __name__ == "__main__":
    args = my_parser.parse_args()
    # print(vars(args))
    # print(parse_browser_args(args.browser_args))
    HEIGHT = args.height
    WIDTH = args.width
    BROWSER = args.browser
    BROWSER_ARGS = parse_browser_args(args.browser_args)
    URL = args.url
    DELAY = args.wait
    
    if (args.use_local):
        os.environ['WDM_LOCAL'] = '1'

    MY_DRIVER = BrowserHelper(browser=BROWSER, arguments=BROWSER_ARGS).auto()
    MY_DRIVER.get(URL)
    if HEIGHT != None and WIDTH != None:
        MY_DRIVER.set_window_rect(height=HEIGHT, width=WIDTH)
    sleep(DELAY)
    MY_DRIVER.get_screenshot_as_file("screenshot.png")
    MY_DRIVER.quit()

