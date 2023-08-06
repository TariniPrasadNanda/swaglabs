import time
import allure
import logging

from allure_commons.types import AttachmentType

log = logging.getLogger(__name__)

@allure.severity(allure.severity_level.CRITICAL)
def test_login_standard_user(initialize_driver):
    driver = initialize_driver
    log.info("Sending username")
    driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
    log.info("Sending password")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    log.info("Clicking on login button")
    driver.find_element("xpath", "//input[@id='login-button']").click()
    driver.implicitly_wait(5)
    assert driver.find_element("xpath", "//div[contains(text(),'Swag Labs')]")
    time.sleep(2)
    driver.find_element("xpath", "//button[@id='react-burger-menu-btn']").click()
    time.sleep(2)
    driver.find_element("xpath", "//a[@id='logout_sidebar_link']").click()
    time.sleep(2)

@allure.severity(allure.severity_level.CRITICAL)
def test_login_lockedout_user(initialize_driver):
    driver = initialize_driver
    driver.find_element("xpath", "//input[@id='user-name']").send_keys("locked_out_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@id='login-button']").click()
    driver.implicitly_wait(10)
    assert driver.find_element("xpath", "//h3[@data-test='error']")
    allure.attach(driver.get_screenshot_as_png(), name="testloginscreen",
                      attachment_type=AttachmentType.PNG)

    time.sleep(5)

@allure.severity(allure.severity_level.MINOR)
def test_login_problem_user(initialize_driver):
    driver = initialize_driver
    driver.find_element("xpath", "//input[@id='user-name']").send_keys("problem_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@id='login-button']").click()
    driver.implicitly_wait(5)
    assert driver.find_element("xpath", "//div[contains(text(),'Swag Labs')]")
    time.sleep(2)
    driver.find_element("xpath", "//button[@id='react-burger-menu-btn']").click()
    time.sleep(2)
    driver.find_element("xpath", "//a[@id='logout_sidebar_link']").click()
    time.sleep(2)

@allure.severity(allure.severity_level.NORMAL)
def test_login_performance_glitch_user(initialize_driver):
    driver = initialize_driver
    driver.find_element("xpath", "//input[@id='user-name']").send_keys("performance_glitch_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@id='login-button']").click()
    driver.implicitly_wait(5)
    assert driver.find_element("xpath", "//div[contains(text(),'Swag Labs')]")
    time.sleep(2)
    driver.find_element("xpath", "//button[@id='react-burger-menu-btn']").click()
    time.sleep(2)
    driver.find_element("xpath", "//a[@id='logout_sidebar_link']").click()
    time.sleep(2)


def test_addtocart(initialize_driver):
    driver = initialize_driver
    driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@id='login-button']").click()
    driver.find_element("xpath", "//input[@id='login-button']").click()
    driver.find_element("xpath", "//input[@id='login-button']").click()



    driver.implicitly_wait(5)
    assert driver.find_element("xpath", "//div[contains(text(),'Swag Labs')]")
    time.sleep(2)
    driver.find_element("xpath", "//button[@id='react-burger-menu-btn']").click()
    time.sleep(2)
    driver.find_element("xpath", "//a[@id='logout_sidebar_link']").click()
    time.sleep(2)
