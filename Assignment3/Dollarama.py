import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a new instance of Chrome WebDriver
driver = webdriver.Chrome()

driver.maximize_window()

# Open the Dollarama website
driver.get("https://www.dollarama.com/")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Dollarama"))

time.sleep(5)

# Element-1: Find sign in/registration Tab
SignIn_Tab = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div/header-widget/div/a[1]")
SignIn_Tab.click()

# Wait for demonstration purposes
time.sleep(3)  # Wait for search results to load

# Element-2: Find the email input field and enter the email address
email_input = driver.find_element(By.XPATH, "/html/body/div[2]/login-section/div/div[1]/div[2]/form/div[1]/input")
email_input.send_keys("navopir616@bacaki.com")

# Wait for demonstration purposes
time.sleep(3)  # Wait for search results to load

# Element-3: Enter "password" in password field
password_field = driver.find_element(By.XPATH, "/html/body/div[2]/login-section/div/div[1]/div[2]/form/div[2]/input")
password_field.send_keys("Hello@123")
time.sleep(3)  # Wait for search results to load

# Element-4: Find the Sign-in button and click it
SignIn_button = driver.find_element(By.XPATH, "/html/body/div[2]/login-section/div/div[1]/div[2]/button")
SignIn_button.click()

# Wait for the page to load
time.sleep(3)  # Wait for search results to load

# Element-5: Click on the career tab
career_tab = driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/div[1]/div[1]/div[6]/a")
career_tab.click()

time.sleep(3)  # Wait for search results to load

# Element-6: Click on the teamleader job button
Teamleader_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/button")
Teamleader_button.click()

time.sleep(3)  # Wait for search results to load

# Navigate back to the home page
driver.get("https://www.dollarama.com/")

# Wait for the page to load
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div/div[4]/header-searchbar/div/form/div/div/input")
search_bar.send_keys("towels")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Add a Product to the Cart (Example: Adding the first product found)
add_to_cart_button = driver.find_element(By.XPATH, "/html/body/category-page/div/div/div[2]/div[3]/div[1]/div/div[3]/button")
add_to_cart_button.click()

# Wait for the product to be added to the cart
time.sleep(3)

# Navigate back to the home page
driver.get("https://www.dollarama.com/")

# Wait for the page to load
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div/div[4]/header-searchbar/div/form/div/div/input")
search_bar.send_keys("Glasses")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)


# Wait for the checkout process (this step depends on the website's checkout flow)
time.sleep(5)

# Close the WebDriver session
driver.quit()

