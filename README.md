HackerRank Automation – Auto Push to GitHub
📌 Overview

This project contains a Python automation script that streamlines the process of managing HackerRank solutions. Instead of manually uploading files, the script automatically:

Collects solved challenge scripts (e.g., .py files).

Organizes them into the correct folder structure.

Uses Git to push them into a GitHub repository.

Includes the edgedriver folder required for browser automation (if needed).

This ensures all solutions are version-controlled, backed up, and easily shareable.

⚡ Features

✅ Automates repetitive Git commands (add → commit → push).

✅ Supports saving HackerRank solutions consistently.

✅ Handles both scripts and dependency folders (e.g., edgedriver).

✅ Helps track coding progress directly in GitHub.

🛠️ Tech Stack

Language: Python 3.x

Tools/Libraries:

os, subprocess (for automation)

git (for version control)

selenium (if using edgedriver for browser tasks)

📂 Project Structure
📦 HackerRank_Automation
 ┣ 📂 edgedriver/         # WebDriver dependency (if used for automation)
 ┣ 📂 solutions/          # Folder containing solved HackerRank scripts
 ┣ 📜 automation.py       # Main Python automation script
 ┣ 📜 README.md           # Project documentation

🚀 How It Works

Place your solved HackerRank scripts into the solutions/ folder.

Run the automation script:

python automation.py


The script will:

Stage new files.

Commit changes with a timestamp message.

Push everything to your GitHub repository.

🎯 Why This Project

Saves time by removing the need for manual uploads.

Keeps coding practice organized and transparent.

Demonstrates automation, Python scripting, and GitHub workflows.

📌 Future Improvements

Add support for multiple coding platforms (LeetCode, Codeforces, etc.).

Enable auto-sorting by problem category (e.g., SQL, Algorithms, Data Structures).

Add CI/CD for automatic repository updates.
