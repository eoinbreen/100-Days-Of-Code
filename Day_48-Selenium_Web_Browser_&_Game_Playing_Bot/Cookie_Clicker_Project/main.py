from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Hello, I am the Cookie Clicker Bot, I play the Cookie Clicker game")

runtime = input("How long (in seconds) would you like me to run for? ")
while not runtime.isdigit():
    print("That is not a valid input, please give a number with no commas")
    runtime = input("How long (in seconds) would you like me to run for? ")


interval = input("How long (in seconds) would you like me to wait in between buying upgrades? "
                 "This will increase automatically as the game goes on : ")
while not interval.isdigit():
    print("That is not a valid input, please give a number with no commas")
    interval = input("How long (in seconds) would you like me to wait in between buying upgrades? "
                     "This will increase automatically as the game goes on : ")
runtime = int(runtime)
interval = int(interval)

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


def check_score():
    with open("high_score.txt", mode="r") as file:
        high_score = int(file.read())
    cps = int(driver.find_element(By.ID, "cps").text.split()[-1])

    if cps > high_score:
        high_score = cps
        print(f"You made {cps} cookies per second, that's a new high score. Good Job!")
    elif cps == high_score:
        print(f"You made {cps} cookies per second, you matched the high score.")
    else:
        print(f"You made {cps} cookies per second, the high score is {high_score}. Have another try to beat it")

    with open("high_score.txt", mode="w") as file:
        file.write(str(high_score))


upgrade_timer = 10

time_start = time.time()


while time.time() < time_start + runtime:
    cookie.click()
    if int(time.time()) == int(time_start + upgrade_timer):
        buy_upgrades()
        upgrade_timer = upgrade_timer + interval
        interval = interval + 0.2

check_score()




