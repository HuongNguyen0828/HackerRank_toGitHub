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

