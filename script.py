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



# --- 4. Extract code from Span text---
spans = driver.find_elements(By.TAG_NAME, "span")
capture = False
code_lines = []

start_keywords = ['Oracle', 'MySQL', 'DB2', 'MS SQL Server']

for s in spans:
    try:
        text = s.text.strip()
        if not text:
            continue

        # Start capturing after seeing any of the DB names
        if any(db in text for db in start_keywords):
            capture = True
            continue  # skip the DB name itself

        # Stop capturing when we see 'Line:'
        if text.startswith("Line:"):
            break

        # Capture code lines
        if capture:
            code_lines.append(text)

    except StaleElementReferenceException:
        continue  # ignore if element disappears

# Combine lines into full code
code = "\n".join(code_lines)
print("✅ Extracted code:\n", code)

# --- 6. Save code to file ---
# Step 1: Extract all span texts
span_texts = []
for s in all_spans:
    try:
        text = s.text.strip()
        if text:
            span_texts.append(text)
    except StaleElementReferenceException:
        continue

# Step 2: Find 'Prepare' index
try:
    start_idx = span_texts.index("Prepare") + 1
except ValueError:
    start_idx = 0

# Step 3: Collect only meaningful problem hierarchy spans
hierarchy = []
for text in span_texts[start_idx:]:
    # Stop if span looks like UI info (numbers, 'points', 'Rank', etc.)
    if any(keyword in text for keyword in ["points", "Rank:", "|", "away", "Try", "Certify", "Compete", "Switch"]):
        break
    hierarchy.append(text)

print("📂 Extracted problem hierarchy:", hierarchy)

# --- 3. Build dynamic folder & file ---
base_folder = "./HackerRank"

if hierarchy:
    folder_path = os.path.join(base_folder, *hierarchy[:-1])  # all but last as folders
    os.makedirs(folder_path, exist_ok=True)
    # Decide file extension dynamically (example: SQL -> .sql, Python -> .py)
    language = hierarchy[0]  # assuming first span indicates language
    ext_map = {"SQL": ".sql", "Python": ".py", "Java": ".java", "C++": ".cpp"}
    file_extension = ext_map.get(language, ".txt")
    filename = os.path.join(folder_path, f"{hierarchy[-1]}{file_extension}")
else:
    # fallback
    filename = os.path.join(base_folder, "solution.txt")

print("💾 File will be saved as:", filename)

# --- 4. Save code ---
with open(filename, "w", encoding="utf-8") as f:
    f.write(code)
print(f"💾 Saved code to {filename}")

# # --- 7. Quit driver ---
# driver.quit()

# Commit and push to GitHub

repo_path = "./HackerRank"
os.chdir(repo_path)

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Auto-update from HackerRank"])
subprocess.run(["git", "push", "origin", "main"])