# Credential_Checker
This Python script checks the validity of credentials by attempting to login to websites listed in an Excel file. It utilizes Selenium for web automation and Pandas for handling Excel files.

# Features
+ Reads website URLs, usernames, and passwords from an Excel sheet.
+ Opens a Chrome browser window and attempts to login to each website using the provided credentials.
+ Checks if login was successful and stores the working credentials in an Excel file.
+ Modified with webdriver delay. It is useful for working with slow internet connection.
+ It autodetects most of the website's login elements.

# Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/madhu-chennu/Credential_Checker.git
```
2. Install the required Python packages:
```
pip install pandas selenium openpyxl
```
3. Download the ChromeDriver executable and place it in the repository directory.

# Usage
1. Prepare an Excel file with the following columns: Website_URL, Username, Password.
2. Update the input_file_path variable in the script to point to your Excel file.
3. Run the script:
```
python Credential_Checker.py
```
4. Check the console output for login status.
5. Working credentials will be saved to a file named working_credentials.xlsx in the same directory.


Get the Chrome webdriver according to your spec 
https://getwebdriver.com/chromedriver#stable

you can check the version of your chrome in settings>help>about.
  I used VScode with the following integrations
  selenium
  pandas
  openpyxl
  python

  I additionally upload another modified version where you can replace the user name and password by ID. 
  check the file web_auto_by_id.py
