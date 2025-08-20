from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
import subprocess

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException



# Start browser
driver = webdriver.Edge()

# 1. Open HackerRank & login
driver.get("https://www.hackerrank.com/auth/login")
time.sleep(10)  # <-- give you time to login manually (safer than storing password)

found = False  # Flag to indicate the target text was found
# 2. Wait until submission is accepted
# Locate the button by CSS selector
button_selector = "#codeshell-wrapper > div.clearfix.pmR.pmL.pmB.plT.fixed-hand1.codeshell-footer > div.pull-right > button.btn.btn-primary.bb-submit.ans-submit"

try:
    # Wait for the button to be clickable
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
    )
    print("Button is present and clickable.")

    # Attach a click action (if you want to detect when *you* click it)
    button.click()
    print("Button was clicked!")
    
except Exception as e:
    print("Error:", e)




# 2. Wait for CodeMirror editor to load and extract code
try:
    code_mirror = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#codeshell-wrapper .CodeMirror"))
    )
    code_content = code_mirror.text
    print("✅ Extracted code:\n", code_content)
except TimeoutException:
    print("❌ Code editor did not load in time")






# Commit and push to GitHub

# Creating folder
repo_path = "./HackerRank/SQL"
os.makedirs(repo_path, exist_ok=True) 
os.chdir(repo_path)

subprocess.run(["git", "add", "."], check=True)
try:
    subprocess.run(["git", "commit", "-m", "Auto-update from HackerRank"], check=True)
except subprocess.CalledProcessError:
    print("ℹ️ No changes to commit")

# Push to correct branch
subprocess.run(["git", "push", "origin", "master"], check=True)