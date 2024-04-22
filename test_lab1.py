import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()

    assert driver.current_url == "https://www.ebay.com/"

    driver.find_element(By.ID, 'gh-ac').send_keys("16gb")
    driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()

    list_element = driver.find_elements(By.XPATH, "//span[@role='heading']")
    for item in list_element:
        product_name = item.text
    prize_of_elements = driver.find_elements(By.XPATH, "// span[@class ='s-item__price']")
    prize = []
    for item in prize_of_elements:
        text = item.text
        # print(text)
        # Remove "$" and any leading/trailing spaces
        x = text.replace("$", "").strip()
        prize.append(x)
    prize.sort()
    print(f"Product having: {prize[1]}")

    driver.quit()
