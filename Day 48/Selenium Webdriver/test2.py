from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Shivansh")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Gupta")

email = driver.find_element(By.NAME, value="email")
email.send_keys("shivanshsg25@gmail.com")

button = driver.find_element(By.TAG_NAME, value="button")
button.click()
