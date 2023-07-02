from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Allows webpage to remain open when program finishes
driver = webdriver.Chrome(options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

history = driver.find_element(By.LINK_TEXT, "View history")
# history.click()

searchbar = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
searchbar.send_keys("Python")
searchbar.send_keys(Keys.ENTER)


