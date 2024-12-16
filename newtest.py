from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

print("Script started")

# Configure WebDriver options
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # Path to the Chromium binary
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")  # Disable sandboxing
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
try:
    # Open the webpage
    driver.get("https://account.proton.me/mail")
    print("on the website")
except Exception as e:
    print("Element not found first:", str(e))


# Clean up
driver.quit()
