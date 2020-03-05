from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.youtube.com/')

username = driver.find_element_by_xpath('//*[@id="search"]')
username.send_keys('telugu movies')	
#//*[@id="search-icon-legacy"]

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
