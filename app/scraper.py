import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from xvfbwrapper import Xvfb
from pyvirtualdisplay import Display

def run_scraper(id):
    display = Display(visible=0, size=(1024, 768))
    display.start()
    #vdisplay = Xvfb()
    #vdisplay.start()

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--allow-running-insecure-content')
    #chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    #chrome_options.add_argument('window-size=1024x768')
    chrome_bin = os.getenv('GOOGLE_CHROME_SHIM', None)
    chromedriver_path = '/usr/local/bin/chromedriver'

    service_log_path = "{}/chromedriver.log".format('/var/www/logs/')
    service_args = ['--verbose']

    if(chrome_bin):
        chromedriver_path = '.chromedriver/bin/chromedriver'
        chrome_options.binary_location = '.apt/usr/bin/google-chrome-stable'
        browser = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options)
    else:
                chrome_options.binary_location = '/usr/bin/google-chrome-stable'
        browser = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options,service_args=service_args,
            service_log_path=service_log_path)

    url = "https://www.youtube.com/live_chat?v=" + str(id)
    browser.get(url)
    browser.implicitly_wait(1)
    #innerHTML = browser.execute_script("return document.body.innerHTML")
    chats = []
    for chat in browser.find_elements_by_css_selector('yt-live-chat-text-message-renderer'):
        author_name = chat.find_element_by_css_selector("#author-name").get_attribute('innerHTML')
        message = chat.find_element_by_css_selector("#message").get_attribute('innerHTML')
        author_name_encoded = author_name.encode('utf-8').strip()
        message_encoded = message.encode('utf-8').strip()
        obj = json.dumps({'author_name': author_name_encoded, 'message': message_encoded })
        chats.append(json.loads(obj))

    browser.quit()
    display.stop()
    #vdisplay.stop()
    return chats

