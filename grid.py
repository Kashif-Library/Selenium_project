from selenium import webdriver
import time

hub_url = "http://192.168.239.130:4444/wd/hub"
driver = webdriver.Remote(command_executor=hub_url, options=webdriver.ChromeOptions())

driver.get("http://stage.alnafi.com")
driver.maximize_window()
driver.implicitly_wait(5)

print(driver.title)
time.sleep(5)
driver.quit()
