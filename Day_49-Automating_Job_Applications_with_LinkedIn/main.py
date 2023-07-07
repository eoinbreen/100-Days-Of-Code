from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Allows webpage to remain open when program finishes
options.add_argument("--start-maximized")  # Fullscreen
driver = webdriver.Chrome(options=options)

driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Dublin%2C%20County%20Dublin%2C%20Ireland&geoId=105178154&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

username = "e.breen185@gmail.com"
password = os.environ.get("linkedin_password")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

username_field = driver.find_element(By.ID, "username")
username_field.send_keys(username)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

time.sleep(3)
job_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable a")
for job in job_list:
    job.click()
    time.sleep(1)

    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()

    follow_button = driver.find_element(By.CLASS_NAME, "follow")
    follow_button.click()


