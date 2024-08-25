from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
driver.get(url)

cookie = driver.find_element(By.ID, "cookie")

five_min = time.time() + 1 * 60
time_out = time.time() + 5

items = driver.find_elements(By.CSS_SELECTOR, "#store .grayed")
items = items[:8]
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time.time() > time_out:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        all_prices = all_prices[:8]
        prices = []
        for price in all_prices:
            price_text = price.text.split("-")[1].strip()
            prices.append(int(price_text.replace(",", "")))

        cookie_upgrades = {}
        for i in range(len(prices)):
            cookie_upgrades[prices[i]] = item_ids[i]

        money_element = driver.find_element(By.ID, "money").text
        money_count = int(money_element.replace(",", ""))

        affordable_upgrades = {}
        for cost, ids in cookie_upgrades.items():
            if money_count > cost:
                affordable_upgrades[cost] = ids

        highest_price_in_affordable_upgrades = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_in_affordable_upgrades]

        driver.find_element(By.ID, value=to_purchase_id).click()

        time_out = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, value="cps")
        print(cookie_per_sec.text)
        break

driver.quit()
