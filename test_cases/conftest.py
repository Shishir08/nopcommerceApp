from pytest_metadata.plugin import metadata
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    driver=None
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching Chrome Browser")
    elif browser=='safari':
        driver=webdriver.Safari()
        print("launching Safari Browser")
    else:
        driver = webdriver.Chrome()

    return driver




def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#adding environment info to HTML report
def pytest_configure(config):
    # config._metadata['Project Name']='nop Commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Shishir'
    config._metadata={
        "Project Name":"nop Commerce",
        "Module Name":"Customers",
        "Tester":"Shishir",

    }


#Delete/Modify environment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


