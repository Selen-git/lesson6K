from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = "standart_user"
password = "secret_sauce"
driver.find_element_by_id("user_name").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("login-button").click()

items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
for item in items:
    driver.find_element_by_xpath(f"//div[text()='{item}']/following-sibling::div/button").click()

driver.find_element_by_class_name("shopping_cart_link").click()
driver.find_element_by_id("checkout").click()
driver.find_element_by_id("first-name").send_keys("John")
driver.find_element_by_id("last-name").send_keys("Doe")
driver.find_element_by_id("postal_code").send_keys("12345")
driver.find_element_by_id("continue").click()

total = driver.find_element_by_class_name("summary_subtotal_label").text

expected_total = "$58.29"
if total == expected_total
    print("Итоговая сумма верна:", total)
else
    print("Ошибка: Итоговая сумма не равна ожидаемой.")

driver.quit()
