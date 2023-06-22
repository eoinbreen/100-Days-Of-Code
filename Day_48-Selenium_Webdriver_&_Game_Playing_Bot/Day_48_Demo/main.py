from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()

# driver.get("https://www.amazon.co.uk/Samsung-Galaxy-Android-Smartphone-Phantom/dp/B09NRRVPZ7/ref=sr_1_3?crid=2JF3OKZJBLW8C&keywords=samsung+galaxy+s22&qid=1687206141&sprefix=samsung+galaxy+s22%2Caps%2C77&sr=8-3")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print("Price: " + price.text)


# driver.get("https://www.python.org/")
# searchbar = driver.find_element(By.NAME, "q")
# print(searchbar.get_attribute("placeholder"))

# driver.get("https://www.python.org/")
# link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(link.text)


driver.get("https://www.python.org/")
xpath = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(xpath.text)
