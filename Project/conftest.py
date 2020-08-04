import pytest
from selenium import webdriver
from Project.common.factories.driver_factory import DriverFactory
import urllib3
import warnings
from _pytest.runner import CallInfo
from _pytest.terminal import TerminalReporter
import sys



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
    "browserName":"chrome"
}
#"version":"84.0",
#"enableVNC": False,
#"enableVideo": False,
#"javascriptEnabled": True

firefoxCapabilities = {
    "browserName":"firefox"
}


@pytest.fixture(params=[chromeCapabilities, firefoxCapabilities])
def capabilities(request):
    return request.param


@pytest.fixture(scope="function")
def driver(request, capabilities):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    driver = webdriver.Remote(command_executor='http://localhost:20500/wd/hub', desired_capabilities=capabilities)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()



@pytest.fixture(scope="function")
def title_of_test():
    pass