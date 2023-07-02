from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Allows webpage to remain open when program finishes
driver = webdriver.Chrome(options=options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Eoin")

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Breen")

email = driver.find_element(By.NAME, "email")
email.send_keys("e.breen185@gmail.com")

button = driver.find_element(By.XPATH, "/html/body/form/button")
button.click()


