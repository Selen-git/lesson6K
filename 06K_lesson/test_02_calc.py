from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_input.clear()
delay_input.send_keys("45")

driver.find_element(By.CSS_SELECTOR, "button#seven").click()

driver.find_element(By.CSS_SELECTOR, "button#add").click()

driver.find_element(By.CSS_SELECTOR, "button#eight").click()

driver.find_element(By.CSS_SELECTOR, "button#equal").click()

result = driver.find_element(By.CSS_SELECTOR, "p#result")
assert result.text == "15"
