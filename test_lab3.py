import random
import string
import time
import pdb
import allure
import pytest
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Registrationpage():
    @allure.title("Registration_Page")
    @allure.description("#TC1- Verify URL and get list of product after searching keyword")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Nilesh Nikume")
    @allure.link("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage", name="Website")
    @allure.testcase("TC-1")
    @pytest.mark.smoke
    def test_open_login(self):
        driver = webdriver.Chrome()
        driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
        driver.maximize_window()

        assert driver.current_url == "https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage"
        allure.attach(driver.get_screenshot_as_png(), name='CDPEN_Home_Page_Screenshot',
                      attachment_type=AttachmentType.PNG)

        driver.switch_to.frame(driver.find_element(By.ID, "result"))
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        allure.attach(driver.get_screenshot_as_png(), name='CDPEN_Registration_Page01_Screenshot',
                      attachment_type=AttachmentType.PNG)
        User_Name_Error_Message = driver.find_element(By.XPATH,
                                                      "//*[text()='Username must be at least 3 characters']").text
        Emai_Error_Message = driver.find_element(By.XPATH, "//*[text()='Email is not invalid']").text
        Password_Error_Message = driver.find_element(By.XPATH,
                                                     "//*[text()='Password must be at least 6 characters']").text
        Confirm_Password_Error_Message = driver.find_element(By.XPATH, "//*[text()='Password2 is required']").text

        if User_Name_Error_Message == "Username must be at least 3 characters" and Emai_Error_Message == "Email is not invalid" and Password_Error_Message == "Password must be at least 6 characters" and Confirm_Password_Error_Message == "Password2 is required":
            assert True, "Enter All Mandatory fields"
        else:
            assert False

        password = random_password()
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(Generate_Email())
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='password2']").send_keys(password)

        allure.attach(driver.get_screenshot_as_png(), name='CDPEN_Registration_Page_Screenshot',
                      attachment_type=AttachmentType.PNG)

        assert (driver.find_element(By.XPATH, "//input[@id='username']/following::small").text
                == "Username must be at least 3 characters")

        driver.quit()


def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))  # random 4 char lower case e.g gfhd
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])  #
    return f"{username}@{domain}"  # random 4 char + domain


def random_password():
    characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    password = ''.join(random.choices(characters, k=8))
    return password
