from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://mywipro.wipro.com/')

username = driver.find_element_by_xpath('//*[@id="i0116"]')
username.send_keys('hhh')	