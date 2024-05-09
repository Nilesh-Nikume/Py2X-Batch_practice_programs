import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_Orange_hrm_login_page:

    def test_loging_page(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

        driver.implicitly_wait(5)
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # print(driver.current_url)
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
        time.sleep(3)
        element_icons = driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
        print(element_icons)
        element_userrole_icon = element_icons[0]
        element_userrole_icon.click()
        driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()

        element_status_icon = element_icons[1]
        element_status_icon.click()
        driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()
        time.sleep(5)
        # driver.find_element(By.XPATH, )
        # driver.find_element(By.XPATH, )




