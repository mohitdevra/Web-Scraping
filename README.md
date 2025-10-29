# Web Scraping Project

This project Scrapes data from websites using *Python* and *Selenium WebDriver*.
---

## Setup Instructions

Follow these steps to run this Selenium project on your own system:

###  Install Requirements*

Make sure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Firefox Browser](https://www.mozilla.org/en-US/firefox/new/)
- [pip (Python package manager)](https://pip.pypa.io/en/stable/installation/)

Then install the Python libraries used in this project:
```bash
pip install -r requirements.txt


---

> Install Geckodriver

Selenium needs a driver to control Firefox — called geckodriver.
You can install it manually as follows:

1. Download the correct version for your system:
🔗 https://github.com/mozilla/geckodriver/releases


2. Extract the downloaded file (you’ll get geckodriver.exe).


3. Move it to a safe folder, for example:

C:\WebDrivers\

4. Add that folder to your PATH:

Press Windows + S → search “Environment Variables”

Click “Edit the system environment variables”

Click “Environment Variables…”

Under System variables, find Path → click Edit

Click New → add:

C:\WebDrivers\

Click OK on all windows to save.

5. Test if it’s added correctly:
Open a new Command Prompt and run:

geckodriver --version

If it shows a version, you’re all set ✅


---


> Run the Project

Once everything is ready, open a terminal in your project folder and run:

python main.py

Selenium will launch Firefox automatically and perform the automation defined in your script.


---

> Optional: ChromeDriver Setup

If you want to use Chrome instead of Firefox:

1. Download ChromeDriver from https://chromedriver.chromium.org/downloads


2. Move it to the same folder (C:\WebDrivers\)


3. Add it to PATH the same way


4. Update your code to use:

from selenium import webdriver
driver = webdriver.Chrome()


---

✅ Quick Checklist

Requirement	Installed?

Python 3.8+	
Selenium (via pip install selenium)
Firefox Browser	Geckodriver added to PATH	

---

👨‍💻 Author

Mohit Devra
Python Developer | Web Scraping Expert
🚀 Building practical Web Scraping projects with Selenium and Python

---
