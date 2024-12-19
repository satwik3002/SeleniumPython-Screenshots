from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the website in Chrome
driver = webdriver.Chrome()  # Ensure you have the correct driver installed
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(8)

# Step 3: Enter Email Address and Password, then click the sign-in button
email_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
email_input.send_keys("satwikkatamaraju@gmail.com")  # Replace with your email
time.sleep(5)
driver.save_screenshot("username_screenshot.png")  # Corrected file path
password_input.send_keys("Y2#ssv@Xp/xP8Wt")        # Replace with your password
time.sleep(5)
driver.save_screenshot("password_screenshot.png")  # Corrected file path

sign_in_button = driver.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[2]/button")
sign_in_button.click()
time.sleep(2)
driver.save_screenshot("signin_screenshot.png")  # Corrected file path

# Corrected screenshot saving logic
destinationFileName = "HollandandBarrett"
fileName = str(round(time.time() * 1000)) + ".png"
screenshotDirectory = "./HollandandBarrett"
destinationFile = f"{screenshotDirectory}/{fileName}"  # Correct path concatenation

try:
    driver.save_screenshot(destinationFile)
    print("Screenshot saved to directory --> :: " + destinationFile)
except FileNotFoundError:
    print("Error: Directory does not exist.")

