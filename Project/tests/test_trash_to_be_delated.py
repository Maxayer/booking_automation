from selenium import webdriver
import time

desiredCapabilities={
"browserName":"chrome",
"browserName":"firefox"
}

driver = webdriver.Remote(command_executor='http://localhost:20500/wd/hub',desired_capabilities = desiredCapabilities)
driver.get("https://www.google.co.in/")
print(driver.title)
time.sleep(5)
driver.quit()