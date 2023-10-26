# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from add_to_group import csv_to_string  # Import function to convert CSV to string
import sys

# Load member data from CSV using the 'csv_to_string' function
#members = csv_to_string(f'"C:\Users\91766\Desktop\{sys.argv[3]}"')

# Initialize the function to add participants to a WhatsApp group
def add_participants_to_group(ph_no: str, group_name: str):#, member_string: str):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()

    # Open the WhatsApp Web URL
    driver.get("https://web.whatsapp.com/")
    driver.implicitly_wait(15)  # Implicitly wait for elements to load

    # Locate and click the login link
    login = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Link with phone number']")))
    login.click()
    driver.implicitly_wait(10)

    # Locate the phone number input field, enter 'ph_no', and press RETURN
    phone_number = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div[3]/div[2]/div/div/div/form/input')
    phone_number.send_keys(ph_no)
    phone_number.send_keys(Keys.RETURN)

    driver.implicitly_wait(2000)  # Wait for WhatsApp to load

    # Locate the search bar and search for the 'group_name'
    search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]')
    search.send_keys(group_name)
    search.send_keys(Keys.RETURN)

    driver.implicitly_wait(600)  # Wait for search results to load

    # Click on the group chat to open it
    tab = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]')
    tab.click()
    driver.implicitly_wait(200)  # Wait for the chat to open

    # Locate and click the "Add participants" button
    add_participants = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[7]/div[2]/div[1]')
    add_participants.click()

    driver.implicitly_wait(200)  # Wait for the participants section to load

    # Locate and click the participant search bar
    participant_search = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p')
    participant_search.click()

    # String of participants to be added (replace with 'member_string' variable)
    participant_str = "person_1 person_2 person_3"

    # Loop through the participant string and add participants
    count = 0
    for participant in participant_str:
        if participant != ' ':
            participant_search.send_keys(participant)
        else:
            participant_search.send_keys(Keys.ENTER)
            count += 1
            participant_search.send_keys(Keys.BACKSPACE)


    # Locate and click the "Submit" button to add participants
    submit = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div')
    submit.click()
    driver.implicitly_wait(3)

    # Locate and click the "Sure" button to confirm adding participants
    sure = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]')
    sure.click()

    # Close the browser session
    driver.quit()

    # Print the total number of participants added to the group
    print(f"Total {count} participants added to the {group_name} group!")

# Entry point of the script
if __name__ == '__main__':
    # Call the 'add_participants_to_group' function with appropriate parameters
    add_participants_to_group(ph_no=sys.argv[1], group_name=sys.argv[2])#, member_string=members)
#1 phone, 2 group name 3 file name in csv