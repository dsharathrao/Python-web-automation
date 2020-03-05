from selenium import webdriver

kala = webdriver.Chrome()
kala.maximize_window()
kala.implicitly_wait(20)
kala.get('https://mywipro.wipro.com/')

username = kala.find_element_by_xpath('//*[@id="i0116"]')
username.send_keys('sharrath')	