import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_table_chk():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    prize_elements = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[4]")
    total = []
    for element in prize_elements:
        value = int(element.text)  # Assuming the text represents integers
        total.append(value)
        print(value)

    result_sum = sum(total)
    print(result_sum)
    driver.quit()