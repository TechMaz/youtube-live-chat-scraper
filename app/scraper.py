import json
import os
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def run_scraper(id):
	#display = Display(visible=0, size=(1024, 768))
	#display.start()

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-extensions')
	#chrome_options.add_argument('window-size=1200x600')
	chrome_bin = os.getenv('GOOGLE_CHROME_SHIM', None)
	if(chrome_bin):
		chrome_options.binary_location = '.apt/usr/bin/google-chrome-stable'
		'''
		desired_capabilities = DesiredCapabilities.CHROME
		desired_capabilities['chromeOptions'] = {
    		"binary": '.apt/usr/bin/google-chrome-stable'
		}
		browser = webdriver.Chrome(desired_capabilities=desired_capabilities)
		'''
		browser = webdriver.Chrome(chrome_options=chrome_options)
	else:
		#chrome_options.add_argument('window-size=1200x600')
		browser = webdriver.Chrome(chrome_options=chrome_options)

	url = "https://www.youtube.com/live_chat?v=" + str(id)
	browser.get(url)
	browser.implicitly_wait(1)
	#innerHTML = browser.execute_script("return document.body.innerHTML")
	chats = []
	for chat in browser.find_elements_by_css_selector('yt-live-chat-text-message-renderer'):
		message = chat.find_element_by_css_selector("#message").get_attribute('innerHTML')
		chats.append(("{ message: '" + message.encode('utf-8').strip() +"' },"))

	browser.quit()
	#display.stop()
	return chats