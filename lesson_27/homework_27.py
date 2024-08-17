from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver = webdriver.Firefox()
driver.get('http://localhost:8000/dz.html')
driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
input_field_1 = driver.find_element(By.XPATH, '//input[@id="input1"]')
input_field_1.send_keys("Frame1_Secret")
button_1 = driver.find_element(By.XPATH, '//button[@onclick="verifyInput(\'input1\')"]')
button_1.click()

alert = Alert(driver)

if "Верифікація пройшла успішно!" == alert.text:
    print("Test passed")
else:
    print("Test failed")
alert.accept()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
input_field_2 = driver.find_element(By.XPATH, '//input[@id="input2"]')
input_field_2.send_keys("Frame2_Secret")
button_1 = driver.find_element(By.XPATH, '//button[@onclick="verifyInput(\'input2\')"]')
button_1.click()

alert = Alert(driver)

if "Верифікація пройшла успішно!" == alert.text:
    print("Test passed")
else:
    print("Test failed")
alert.accept()




driver.quit()