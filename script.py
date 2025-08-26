from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os, sys
import subprocess

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException


# Creating folder and save file JUST 1 time 
repo_path = "./HackerRank/SQL"
os.makedirs(repo_path, exist_ok=True) 

## 1. Go inside of repo_path
os.chdir(repo_path) 
### initialize git init
subprocess.run(["git", "init"], check=True)

with open("README.md", "w", encoding="utf-8") as f: 
    f.write("This is a collections of HackerRank problems' soutions!")
subprocess.run(["git", "add", "README.md"], check=True) 
subprocess.run(["git", "branch", "-M", "master"], check=True) 
remote_name = "origin"
remote_url = "https://github.com/HuongNguyen0828/HackerRank_solutions"

# check if remote exists
result = subprocess.run(
    ["git", "remote"],
    capture_output=True,
    text=True
)

remotes = result.stdout.splitlines()

if remote_name in remotes:
    print(f"Remote '{remote_name}' already exists. Doing nothing.")
else:
    subprocess.run(["git", "remote", "add", remote_name, remote_url], check=True)
    print(f"Remote '{remote_name}' added.")

## first push 
subprocess.run(["git", "push", "-u", "origin", "master"], check=True)
# Commit and push to GitHub
subprocess.run(["git", "add", "."], check=True)
try:
    subprocess.run(["git", "commit", "-m", f"Add README.md"], check=True)
except subprocess.CalledProcessError:
    pass

# Start browser
driver = webdriver.Edge()

#### Detecting Submit button is clicked
submit = False
# To keep browser stay
try:
    # 1. Open HackerRank & login
    driver.get("https://www.hackerrank.com/auth/login")
    time.sleep(10)  # <-- give you time to login manually (safer than storing password)
    # keep the Python process alive
    while True:  
        try: 
            # Check if browser window is still open
            driver.current_url
        except:
            print("Browser window closed by user")
            break
        
        # REVERST button submit to be false
        submit = False # to come back to loop
        # Locate the button by CSS selector
        button_selector = "#codeshell-wrapper > div.clearfix.pmR.pmL.pmB.plT.fixed-hand1.codeshell-footer > div.pull-right > button.btn.btn-primary.bb-submit.ans-submit"

        while not submit:
            try:
                # Wait for the button to be clickable
                button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
                )
                print("Button is present and clickable.")

                # if detect clicked, Inject JavaScript that attaches a click listener to the button
                driver.execute_script("""
                    const btn = arguments[0];
                    btn.addEventListener("click", () => {
                        btn.setAttribute("data-was-clicked", "true");
                    });
                """, button)

                # Listening for the click 
                while True:
                    clicked = button.get_attribute("data-was-clicked")
                    if clicked == "true":
                        print("Button was manually clicked!")
                        submit = True

                        # Remove the attribute after detecting the click
                        driver.execute_script("""
                            const btn = arguments[0];
                            btn.removeAttribute("data-was-clicked");
                        """, button)
                        break
            except Exception as e:
                print("Error:", e)

        if submit:
            # 2. Wait for CodeMirror editor to load and extract code
            try:
                code_mirror = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#codeshell-wrapper .CodeMirror"))
                )

                # Each line of code is usually inside div.CodeMirror-line
            # Get each line's text
                lines = code_mirror.find_elements(By.CSS_SELECTOR, "div > pre")
                code_lines = []

                for line in lines:
                    text = line.text.rstrip("\n")
                    code_lines.append(text)

                # Join into final code
                code_content = "\n".join(code_lines)
                print("✅ Extracted code:\n", code_content)
            except TimeoutException:
                print("❌ Code editor did not load in time")

            # Save code into file solution
            # 1. Extract file_name
            breadcrumb_spans = driver.find_elements(
                By.CSS_SELECTOR,
                "ol.community-breadcrumb li.breadcrumb-item span.breadcrumb-item-text"
            )

            # Take the last one
            last_span = breadcrumb_spans[-1]
            problem_name = last_span.text
            filename = problem_name + ".sql"
            print("💾 File will be saved as:", filename)
            # --- 4. Save code --- 
            # Extract lang: Locate the span inside the container by CSS selector
            span_element = driver.find_element(By.CSS_SELECTOR, "#s2id_select-lang span")
            language_text = '--' + span_element.text # adding language as command


            with open(filename, "w", encoding="utf-8") as f: 
                f.write(language_text) # Adding languange on the top of the file
                f.write(code_content) 
                print(f"💾 Saved code to {filename}")

            # Commit and push to GitHub
            subprocess.run(["git", "add", "."], check=True)
            try:
                subprocess.run(["git", "commit", "-m", f"Auto-Add {filename} from HackerRank"], check=True)
            except subprocess.CalledProcessError:
                print("ℹ️ No changes to commit")
            # Push to correct branch
            try:
                subprocess.run(["git", "push"], check=True)
            except subprocess.CalledProcessError:
                print("Push failed, trying pull + push...")
                subprocess.run(["git", "pull", "--rebase"], check=True)
                subprocess.run(["git", "push"], check=True)
            print("🎉 Script finished. Browser will remain open. Press Ctrl+C to exit manually.")

except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    try:
        driver.quit()
    except:
        pass
    sys.exit(0)