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

# To keep browser stay
try:
    while True:
        time.sleep(1)  # keep the Python process alive
        found = False  # Flag to indicate the target text was found
        # 2. Wait until submission is accepted
        # Locate the button by CSS selector
        button_selector = "#codeshell-wrapper > div.clearfix.pmR.pmL.pmB.plT.fixed-hand1.codeshell-footer > div.pull-right > button.btn.btn-primary.bb-submit.ans-submit"

        while not found:
            try:
                # Wait for the button to be clickable
                button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
                )
                print("Button is present and clickable.")

                # Inject JavaScript that attaches a click listener to the button
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
                        found = True
                        break
                    time.sleep(0.5)
                
            except Exception as e:
                print("Error:", e)




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
                text = line.text.strip()
                code_lines.append(text)

            # Join into final code
            code_content = "\n".join(code_lines)
            print("✅ Extracted code:\n", code_content)
        except TimeoutException:
            print("❌ Code editor did not load in time")



        # Creating folder and save file
        repo_path = "./HackerRank/SQL"
        os.makedirs(repo_path, exist_ok=True) 

        ## 1. Go inside of repo_path
        os.chdir(repo_path) 

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


        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        try:
            subprocess.run(["git", "commit", "-m", f"Auto-update adding {filename} from HackerRank"], check=True)
        except subprocess.CalledProcessError:
            print("ℹ️ No changes to commit")



        # Push to correct branch
        # Check existing remotes
        remotes = subprocess.run(["git", "remote"], capture_output=True, text=True)
        if "origin" in remotes.stdout.split():
            print("⚠️ Remote 'origin' already exists, just push")
            subprocess.run(["git", "push", "--set-upstream", "origin", "master"])
            

        else: # Add remote
            subprocess.run(["git", "remote", "add", "origin", "https://github.com/HuongNguyen0828/HackerRank_solutions"], check=True)
            print("✅ Remote 'origin' added successfully")
            # Push commit
            ##Before pushing, pull the remote changes and merge them:
            subprocess.run(["git", "pull", "--rebase", "origin", "master"], check=True) 
            subprocess.run(["git", "push", "origin", "master"], check=True)

        print("🎉 Script finished. Browser will remain open. Press Ctrl+C to exit manually.")


except KeyboardInterrupt:
    print("Exiting...")  # user pressed Ctrl+C