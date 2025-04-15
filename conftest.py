import pytest
from selenium import webdriver
import os

# To run this test file, run the following command in the terminal:
# python -m pytest test_e2eFrameworkTest1.py --browser_name Chrome
# python -m pytest test_e2eFrameworkTest1.py --browser_name=chrome --html=report.html -s -v
#python -m pytest --browser_name=firefox --html=report.html -s -v 


# This is a necessary step to add the command line option to pytest,
def pytest_addoption(parser): 
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection") 

@pytest.fixture(scope="function")
def browserInstance(request):  # the request object is used to get the command line options passed to pytest
    browser_name = request.config.getoption("browser_name")  # --browser Chrome is the command line option passed to pytest
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")  # this will open the url in the browser
    request.node.driver = driver  # Save driver to the test item for screenshot
    yield driver  # This will return the driver instance to the test function, will run before test function execution
    driver.close()  # This will close the browser after the test is completed


# 🔽 Screenshot hook (added separately, your original code is untouched)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    
    # Only take screenshot on failures
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.png(screenshot_path))
            else:
                report.extra = [pytest_html.extras.png(screenshot_path)]


# Needed to access `pytest_html` in the hook
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")
