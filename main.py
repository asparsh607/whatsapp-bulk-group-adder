from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from add_to_group import csv_to_string
import time

members = csv_to_string('contact_to_be_extracted.csv')


#edge_options = Options()
#edge_options.add_argument('--blink-settings=imagesEnabled=false')
# Initialize the Edge webdriver


def add_participants_to_group(ph_no: str, group_name: str, member_list: list):
    driver = webdriver.Chrome()

    driver.get("https://web.whatsapp.com/")
    driver.implicitly_wait(15)

    login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Link with phone number']")))

    login.click()
    driver.implicitly_wait(10)

    phone_number = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div[3]/div[2]/div/div/div/form/input')
    phone_number.send_keys(ph_no)
    phone_number.send_keys(Keys.RETURN)

    driver.implicitly_wait(2000)

    search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]')
    search.send_keys(group_name)
    search.send_keys(Keys.RETURN)

    driver.implicitly_wait(600)

    tab = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]')
    tab.click()
    driver.implicitly_wait(200)

    add_participants = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[7]/div[2]/div[1]')
    add_participants.click()

    driver.implicitly_wait(200)


    participant_search = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p')
    participant_search.click()

    participant_list = ['biraj', 'Sagar', 'Sachin'] #member_list <-- function variable ^^^^^^^^^^^ yaha pe hoga

    for participant in participant_list:
        participant_search.send_keys(participant)
        time.sleep(2)
        participant_search.send_keys(Keys.ENTER)
        time.sleep(2)
        participant_search.send_keys(Keys.BACKSPACE)


    #last command to finally add participants
    submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div')
    submit.click()
    driver.implicitly_wait(3)

    sure = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]')
    sure.click()


    driver.quit()
    print(f"Total {len(participant_list)} participants added to the {group_name} group !")


if __name__ == '__main__':
    add_participants_to_group(ph_no='', group_name='') #member_list=members)