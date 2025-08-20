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
while not found:
    spans = driver.find_elements(By.TAG_NAME, "span")
    for s in spans:
        try:
            if s.text.strip():
                print("SPAN TEXT:", repr(s.text))
            if "Would you like to challenge your friends?" in s.text:
                print("Text found! Breaking loop.")
                found = True
                break
        except StaleElementReferenceException:
            print("Redirecting Message:")




# 2. Wait for CodeMirror editor to load and extract code
try:
    # Locate the editor container
    editor = driver.find_element(By.CSS_SELECTOR, "#codeshell-wrapper .CodeMirror-code")
    
    # Extract each line
    code_lines = editor.find_elements(By.CSS_SELECTOR, "pre > span")
    code_content = "\n".join([line.text for line in code_lines])
    
    print("==== Extracted Code ====")
    print(code_content)

except Exception as e:
    print("Error while extracting code:", e)





# Commit and push to GitHub

repo_path = "./HackerRank"
os.chdir(repo_path)

subprocess.run(["git", "init"], check=True)  # in case repo not initialized
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Auto-update from HackerRank"], check=True)

# Push to correct branch
subprocess.run(["git", "push", "origin", "master"], check=True)