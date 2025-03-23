from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name_field = driver.find_element_by_name("firstname")
first_name_field.send_keys("Иван")

last_name_field = driver.find_element_by_name("lastname")
last_name_field.send_keys("Петров")

address_field = driver.find_element_by_name("address")
address_field.send_keys("Ленина, 55-3")

email_field = driver.find_element_by_name("email")
email_field.send_keys("test@skypro.com")

phone_field = driver.find_element_by_name("phone")
phone_field.send_keys("+7985899998787")

city_field = driver.find_element_by_name("city")
city_field.send_keys("Москва")

country_field = driver.find_element_by_name("country")
country_field.send_keys("Россия")

job_position_field = driver.find_element_by_name("job_position")
job_position_field.send_keys("QA")

company_field = driver.find_element_by_name("company")
company_field.send_keys("SkyPro")

submit_button = driver.find_element_by_id("submit")
submit_button.click()

zip_code_field = driver.find_element_by_name("zipcode")
assert "error" in zip_code_field.get_attribute("class")

field_elements = driver.find_elements_by_class_name("form-control")
for elem in field_elements:
    if elem != zip_code_field:
        assert "success" in elem.get_attribute("class")
