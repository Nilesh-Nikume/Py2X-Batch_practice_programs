import time
import allure
import pytest
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_loginpage():
    @allure.title("Loginpage")
    @allure.description("#TC1- Verify URL and get list of product after searching keyword")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Nilesh Nikume")
    @allure.link("https://www.ebay.com/", name="Website")
    @allure.testcase("TC-1")
    @pytest.mark.smoke
    def test_open_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ebay.com/")
        driver.maximize_window()

        assert driver.current_url == "https://www.ebay.com/"
        allure.attach(driver.get_screenshot_as_png(), name='Home_Page_Screenshot', attachment_type=AttachmentType.PNG)

        driver.find_element(By.ID, 'gh-ac').send_keys("16gb")
        driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()
        allure.attach(driver.get_screenshot_as_png(), name='Product_Page_Screenshot', attachment_type=AttachmentType.PNG)

        list_element = driver.find_elements(By.XPATH, "//span[@role='heading']")
        for item in list_element:
            product_name = item.text
        prize_of_elements = driver.find_elements(By.XPATH, "// span[@class ='s-item__price']")
        prize = []
        for item in prize_of_elements:
            text = item.text
            #    print(text)
            #    Remove "$" and any leading/trailing spaces
            x = text.replace("$", "").strip()
            prize.append(x)
        prize.sort()
        print(f"Product having: {prize[1]}")

        driver.quit()
