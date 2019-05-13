from selenium import webdriver
import random
import time
while 1 > 0:
	myProxy = random.choice(open('IPs.txt').readlines())
	#parts = myProxy.strip().split(":") # strip removes spaces and line breaks
	#host = parts[0]
	#port = int(parts[1]) # port needs to be an integer

	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.autoconfig_url", myProxy)
	#profile.set_preference("network.proxy.http", host)
	#profile.set_preference("network.proxy.http_port", port)
	#profile.update_preferences()

	browser = webdriver.Firefox(firefox_profile=profile)
	browser.get("http://www.greentruppen.it/photogallery/popup/eco-bottiglia...togliere-per-donare")
	browser.execute_script("document.getElementById('likee_5418').click()")
	browser.close()
	time.sleep(20)