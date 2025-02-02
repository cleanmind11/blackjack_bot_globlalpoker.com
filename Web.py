from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Path to your WebDriver (change this to your actual path)
driver_path = r'C:\Users\rocke\Downloads\chromedriver-win64\chromedriver.exe'  # Update this path

# Set up Chrome options to capture network requests
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_experimental_option("perfLoggingPrefs", {
#     "enableNetwork": True,
#     "enablePage": False,
#     "enableTimeline": False,
#     "traceCategories": "devtools.network"
# })
# chrome_options.add_experimental_option("prefs", {
#     "performance": {
#         "network": {
#             "enableNetwork": True
#         }
#     }
# })

# # Set up desired capabilities to capture performance logs
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

# Create a new instance of the Chrome driver using Service
service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service, options=chrome_options, desired_capabilities=desired_capabilities)
driver = webdriver.Chrome(service=service)
# Function to capture and print network requests
# def capture_network_requests():
#     logs = driver.get_log('performance')
#     for log in logs:
#         message = log['message']
#         message = message.replace('{"message":', '').strip().rstrip(',')
#         message = json.loads(message)
#         if message['method'] == 'Network.requestWillBeSent':
#             request = message['params']['request']
#             print(f"Request URL: {request['url']}")
#             print(f"Request Method: {request['method']}")
#             print(f"Request Headers: {request['headers']}")
#             print("-" * 40)

# Open the login page
driver.get('https://play.globalpoker.com/')
time.sleep(10)
# Wait for the email input field to be present
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, '1-email'))
)

# Enter your email
email_input.send_keys('kiranhuxley11@gmail.com')

# Wait for the password input field to be present
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, '1-password'))
)

# Enter your password
password_input.send_keys('123!@#QWErty')

# Wait for the submit button to be clickable
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, '1-submit'))
)

# Click the submit button
submit_button.click()

# Wait for a few seconds to see the result (you can replace this with a more specific wait condition)
time.sleep(10)
# print(driver.page_source)
with open('firstpage.txt', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)
# cookie_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
# )
# cookie_button.click()
time.sleep(5)
casino_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'casino-lobby'))
)
casino_button.click()
time.sleep(5)
# print(driver.page_source)
with open('casinopage.txt', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)
time.sleep(5)
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'search-input'))
)

# Enter your email
search_input.send_keys('blackjack')
# sg_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'refresh-balance-btn'))
# )
# sg_button.click()
time.sleep(5)
# print(driver.page_source)
with open('search.txt', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

blackjack_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'blackjack-classic'))
)
blackjack_button.click()
time.sleep(10)
# print(driver.page_source)
with open('game.txt', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)
game_element = driver.find_element(By.CLASS_NAME, 'gap-slots-game-active')
game_element.click()
actions = ActionChains(driver)
actions.send_keys('1').perform()
actions.send_keys(Keys.SPACE).perform()
# capture_network_requests()
for request in driver.requests:
        if request.response:  # Check if there is a response for the request
            print(
                f"URL: {request.url}\n"
                f"Method: {request.method}\n"
                f"Response Status Code: {request.response.status_code}\n"
                f"Content-Type: {request.response.headers['Content-Type']}\n"
                "-------------------------------------"
            )
time.sleep(15)
# Close the browser
driver.quit()