# HackerRank Automation – Auto Push to GitHub  

## 📌 Overview  
This project contains a **Python automation script** that streamlines the process of managing HackerRank solutions. Instead of manually uploading files, the script automatically:  
- Collects solved challenge scripts (e.g., `.py` files).  
- Organizes them into the correct folder structure.  
- Uses Git to push them into a GitHub repository.  
- Includes the `edgedriver` folder required for browser automation (if needed).  

This ensures all solutions are **version-controlled**, **backed up**, and **easily shareable**.  

---

## ⚡ Features  
- ✅ Automates repetitive Git commands (add → commit → push).  
- ✅ Supports saving HackerRank solutions consistently.  
- ✅ Handles both scripts and dependency folders (e.g., `edgedriver`).  
- ✅ Helps track coding progress directly in GitHub.  

---

## 🛠️ Tech Stack  
- **Language:** Python 3.x  
- **Tools/Libraries:**  
  - `os`, `subprocess` (for automation)  
  - `git` (for version control)  
  - `selenium` (if using `edgedriver` for browser tasks)  

---

## 📂 Project Structure  
