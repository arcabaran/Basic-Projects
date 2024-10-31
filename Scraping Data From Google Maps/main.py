# Import the necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Make browser open in the background
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Specify the path to the chromedriver executable
service = Service("C:/chromedriver_win32/chromedriver.exe")

# Create the webdriver object
browser = webdriver.Chrome(service=service, options=options)

# List of Google Map URLs
url = [
    "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0124687,17z/data=!3m1!4b1!4m5!3m4!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687",
    "https://www.google.com/maps/place/Lucky+Dhaba/@30.653792,76.8165233,17z/data=!3m1!4b1!4m5!3m4!1s0x390feb3e3de1a031:0x862036ab85567f75!8m2!3d30.653792!4d76.818712"
]

# Loop through the URLs
for i in range(len(url)):

    # Open the Google Map URL
    browser.get(url[i])

    # Wait for the page to load and then get the title
    title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "x3AX1-LfntMc-header-title-title"))
    )
    print(i + 1, "-", title.text)

    # Get the rating stars
    stars = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "aMPvhf-fI6EEc-KVuj8d"))
    )
    print("The stars of the restaurant are:", stars.text)

    # Get the description of the place
    description = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "uxOu9-sTGRBb-T3yXSc"))
    )
    print("Description:", description.text)

    # Get the address of the place
    address = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "CsEnBe"))
    )[0]
    print("Address:", address.text)

    # Get the contact number of the place
    phone = address = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "CsEnBe"))
    )[-2]
    print("Contact Number:", phone.text)

    # Get the reviews of the place
    reviews = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "OXD3gb"))
    )
    print("------------------------ Reviews --------------------")
    for review in reviews:
        print(review.text)
    print("\n")

# Close the browser
browser.quit()
