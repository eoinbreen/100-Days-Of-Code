from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Allows webpage to remain open when program finishes
driver = webdriver.Chrome(options=options)

driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Dublin%2C%20County%20Dublin%2C%20Ireland&geoId=105178154&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")