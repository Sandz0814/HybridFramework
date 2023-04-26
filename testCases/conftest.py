from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.ChromiumEdge  # No installed webdriver yet
        print(" Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()  # No installed webdriver yet
        print(" Launching Microsoft Edge")
    else:
        driver = webdriver.Chrome()  # Has a driver and Set as a default browser
    return driver


def pytest_addoption(parser):  # this will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")

######### PYTEST HTML REPORT ########

# It is hook  for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sandro'

# It is hook for Delete/Modify environment info to HTML Report

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


