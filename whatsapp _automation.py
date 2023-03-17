from selenium import webdriver
import time


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
def open():
    chrome_options = Options()

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


    global browser;
    browser = webdriver.Chrome(executable_path=r"C:\Users\ANKIT\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
def send():
    url = 'https://web.whatsapp.com/'

    browser.get(url)

# Set the path of the file you want to send
    file_path = r"C:\Users\ANKIT\Desktop\automation\bb.docx"

# Set the message you want to send
    message = "Here's the file you requested."

# Set the phone number of the recipient
    phone_number = "+917979959844"

# Set the time at which you want to send the message (24-hour format)
    send_hour = 13
    send_min = 30


# Set Chrome options to disable USB devices

# Wait for the user to scan the QR code
    time.sleep(15)
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))

# # Find the element using xpath
# search_box = browser.find_element("xpath","//div[@contenteditable='true'][@data-tab='3']")

# # Use the element to perform actions
# search_box.send_keys(phone_number)

# Select the recipient's contact by phone number
    search_box = browser.find_element("xpath",r'//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    time.sleep(2)
    search_box.send_keys(u'\ue007')
    time.sleep(2)

# Click the attachment button
    attachment_button = browser.find_element("xpath", '//div[@title="Attach"]')
    attachment_button.click()
    time.sleep(5)

# Click the document option
    document_option = browser.find_element("xpath", "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input"
    )
    document_option.send_keys(file_path)
    time.sleep(2)

# Send the file with the specified message
    message_box = browser.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')
    message_box.send_keys(message)
    time.sleep(2)



open()
send