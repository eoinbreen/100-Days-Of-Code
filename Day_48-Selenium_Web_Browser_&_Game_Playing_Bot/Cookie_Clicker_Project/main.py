from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Allows webpage to remain open when program finishes
driver = webdriver.Chrome(options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

runtime = 10   # [seconds] 300 for 5 minutes
interval = 5
time_start = time.time()

while time.time() < time_start + runtime:
    cookie.click()
    if int(time.time()) == int(time_start + interval):
        print(f"{interval} seconds have passed")
        interval = interval + 5



