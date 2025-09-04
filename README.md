# HackerRank Automation – Auto Push to GitHub  

## 📌 Overview  
This project contains a **Python automation script** that streamlines the process of managing HackerRank solutions. Instead of manually uploading files, the script automatically:  
- Collects solved challenge scripts.  
- Organizes them into the correct folder structure. (currently just SQL folder, you can customize as your needs) 
- Uses Git to push them into a GitHub repository.  
- Includes the `edgedriver` folder required for browser automation.  

This ensures all solutions are automatically pushed to GiHub in the same time users submit the solution in HackerRank, so that your solutions are **version-controlled**, **backed up**, and **easily shareable**.  

---

## ⚡ Features  
- ✅ Automates repetitive Git commands (add → commit → push).  
- ✅ Supports saving HackerRank solutions consistently.  
- ✅ Handles challenges name consistenly and automatially matching with HackerRank challenges naming
- ✅ Helps track coding progress directly in GitHub.  

---

## 🛠️ Tech Stack  
- **Language:** Python 3.x  
- **Tools/Libraries:**  
  - `os`, `subprocess` (for automation)  
  - `git` (for version control)  
  - `selenium` (for browser tasks using `edgedriver` )  

---

## 📂 Project Structure 
┣ 📂 edgedriver/ # WebDriver dependency (if used for automation)

┣ 📂 HackerRank/ # Folder containing solved HackerRank scripts

      ┣ 📂 SQL/ # Folder containing solved SQL scripts and commits
  
┣ 📜 script.py # Main Python automation script

┣ 📜 README.md # Project documentation


## 🛡️ Security & Privacy
✅ No Data Collection: no collect or store any of your code or data



✅ Open Source: Full transparency - review our code anytime

## 🚀 How It Works  
1. Clone this repository into your working folder: `clone https://github.com/HuongNguyen0828/HackerRank_toGitHub/`
2. 🖥️ Set Up Microsoft Edge WebDriver


   * **Check your Microsoft Edge version:**  
   [Find your Edge version](https://support.microsoft.com/en-us/microsoft-edge/find-out-which-version-of-microsoft-edge-you-have-c726bee8-c42e-e472-e954-4cf5123497eb)
  * If your version is x86, ** Install msedgedriver.exe file underthe `edgedriver_win32` folder**   

  * If not, **Download the matching WebDriver:**  
   [Microsoft Edge WebDriver Downloads](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads)  

4. **Navigate to the project folder:**  run `cd HackerRank_toGitHub`
5. **Install Python dependencies**: run `pip install selenium``
6. **Set your GitHub repository**:

  * Create a repository to store all HackerRank solutions.
  
  * In script.py, replace the **remote_url** variable with your repository URL: `remote_url = "https://github.com/YourUsername/YourRepoName"`
7. **Run the automation script**: run `python script.py`

✅ And, that’s it! Now, you can login and everytime you submit, your HackerRank solutions will now automatically push to GitHub.
## Future Improvements
* Multi-Language Support: Currently for SQL, expand to capture and organize C++, Java, JavaScript, etc. solutions
* Supporting additional web browsers (e.g., Google Chrome, Firefox, Safari)
* Extending automation to other platforms that don’t natively support saving code to GitHub (e.g., LeetCode).”
     

