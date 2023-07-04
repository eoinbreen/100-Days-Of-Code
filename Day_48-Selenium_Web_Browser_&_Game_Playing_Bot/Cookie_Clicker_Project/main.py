from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Allows webpage to remain open when program finishes
driver = webdriver.Chrome(options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def buy_upgrades():
    money = driver.find_element(By.ID, "money").text
    money = int(money.replace(",", ""))

    best_affordable = ""

    upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    upgrades = upgrades[:-1]  # Take off last element as it comes out as blank

    upgrade_dict = {}

    for upgrade in upgrades:
        name = upgrade.text.split("-")[0].strip()
        cost = int(upgrade.text.split("-")[1].strip().replace(",", ""))  # Remove whitespace and commas
        new_dict = {
            "name": name,
            "cost": cost,
            "link": upgrade
        }

        if money >= cost:
            best_affordable = name

        upgrade_dict[name] = new_dict

    upgrade_dict[best_affordable]["link"].click()


def cookies_per_second():
    cps = driver.find_element(By.ID, "cps").text.split()[-1]
    print(f"You made {cps} cookies per second, good job!")


runtime = 300   # [seconds] 300 for 5 minutes
interval = 5
time_start = time.time()


while time.time() < time_start + runtime:
    cookie.click()
    if int(time.time()) == int(time_start + interval):
        buy_upgrades()
        interval = interval + 5

cookies_per_second()




