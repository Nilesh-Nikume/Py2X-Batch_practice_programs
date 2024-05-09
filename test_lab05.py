from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def test_iframe():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#result"))

    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    time.sleep(2)
    username = driver.find_element(By.ID, "username")
    errormsg = driver.find_element((locate_with(By.TAG_NAME, "small")).below(username)).text
    assert errormsg == "Username must be at least 3 characters"
    time.sleep(3)
