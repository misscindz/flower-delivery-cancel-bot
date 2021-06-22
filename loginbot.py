#!/usr/bin/env python2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import emailFromConfig, passwordFromConfig

email = emailFromConfig
password = passwordFromConfig

browser = webdriver.Chrome()
browser.get(('https://www.freddiesflowers.de/einloggen'))

loginEmail = browser.find_element_by_id('email-address')
loginEmail.send_keys(email)
loginPassword = browser.find_element_by_id('password_32')
loginPassword.send_keys(password)
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/form/div[4]/button").click()

calendar = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Kalender")))
calendar.click()

try:
    bookedDeliveryDays = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".deliverySchedule__calendarCircle--blue")))
    bookedDeliveryDays = browser.find_elements_by_css_selector(".deliverySchedule__calendarCircle--blue")

    unbookedDeliveryDays = 0

    if len(bookedDeliveryDays) > 0 :
        for bookedDay in bookedDeliveryDays:
            bookedDay.click()
            unbookButton = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/section/div/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/button").click()
            unbookedDeliveryDays = unbookedDeliveryDays + 1
except:
    print("No active deliveries found this month.")
finally:
    print("Logging off and closing browser.")
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/a").click()
    browser.close()
    print ´("Done :)")
