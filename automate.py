from datetime import datetime, timedelta
from time import sleep

from playsound import playsound
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

currentTime = datetime.strptime("14/2/2022", '%d/%m/%Y')
print("The current schedule date is " + currentTime.strftime("%d/%m/%Y"))
newTime = currentTime

n = 5000
while n > 1:
    op = webdriver.FirefoxOptions()
    op.add_argument('--headless')
    automateDriver = webdriver.Firefox(options=op)
    automateDriver.get("https://bmvs.onlineappointmentscheduling.net.au/oasis/")  # put here the address of your page
    newIndividualBookingButton = automateDriver.find_element(By.ID, 'ContentPlaceHolder1_btnInd')
    # print(newIndividualBookingButton.get_attribute("class"))
    newIndividualBookingButton.click()

    postCodeInput = automateDriver.find_element(By.ID, 'ContentPlaceHolder1_SelectLocation1_txtSuburb')
    postCodeInput.send_keys('3123')
    postCodeInput.send_keys(Keys.ENTER)

    automateDriver.implicitly_wait(10)

    suburbSelection = automateDriver.find_element(By.XPATH, '//*[@class="tdlocNameTitle"]')
    # print(suburbSelection.text)
    suburbSelection.click()

    # WebDriverWait(automateDriver, 10).until(EC.alert_is_present())
    # automateDriver.switch_to.alert.accept()
    nextButton = automateDriver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_btnCont"]')
    nextButton.click()

    automateDriver.find_element(By.ID, 'chkClass1_489').click()
    automateDriver.find_element(By.ID, 'chkClass1_492').click()

    nextButton = automateDriver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_btnCont"]')
    nextButton.click()

    newTimeRaw = automateDriver.find_element(By.ID, 'ContentPlaceHolder1_SelectTime1_txtAppDate').get_attribute("value")
    if newTimeRaw:
        newTime = datetime.strptime(newTimeRaw, '%d/%m/%Y')
        # print(newTime)
    else:
        newTime = currentTime + timedelta(days=1)

    print("<<< new time " + newTime.strftime("%d/%m/%Y") + " Melbourne")

    if newTime >= currentTime:
        print("😭")
    else:
        playsound('bigbell2.wav')
        print("There is a earlier time, please secure the spot soon")

    sleep(5)
    automateDriver.implicitly_wait(60)
    automateDriver.close()
    n -= 1
