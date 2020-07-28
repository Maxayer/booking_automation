import pytest
from selenium import webdriver
from Project.common.factories.driver_factory import DriverFactory
import urllib3
import warnings


#def pytest_addoption(parser):
    #parser.addoption('--browser_name', action='store', default="chrome",
                     #help="Choose browser: chrome, opera or firefox")


#@pytest.fixture(scope="function")
#def driver(request):
    #browser_name = request.config.getoption("browser_name")
    #driver_factory = DriverFactory(browser_name)
    #driver = driver_factory.get_driver()
    #yield driver
    #driver.quit()


chromeCapabilities = {
    "browserName":"chrome",

}

firefoxCapabilities = {
    "browserName":"firefox"
}

@pytest.fixture(scope="function")
def driver(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    driver = webdriver.Remote(command_executor='http://localhost:20500/wd/hub', desired_capabilities=chromeCapabilities)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_init_2(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    driver = webdriver.Remote(command_executor='http://localhost:20500/wd/hub', desired_capabilities=firefoxCapabilities)
    yield driver
    driver.quit()