import pytest
import time
from Project.common.factories.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver():
    driver_factory = DriverFactory("opera")
    driver = driver_factory.get_driver()
    yield driver
    driver.quit()
