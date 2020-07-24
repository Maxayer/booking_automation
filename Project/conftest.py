import pytest
import time
from Project.common.factories.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, opera or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver_factory = DriverFactory(browser_name)
    driver = driver_factory.get_driver()
    yield driver
    driver.quit()
