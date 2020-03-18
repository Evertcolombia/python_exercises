#!/usr/bin/python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://gmail.com')

emailInput = browser.find_element_by_id('identifierId')
emailInput.send_keys('evertescalante1@gmail.com')

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

passwordInput = browser.find_element_by_css_selector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)')
passwordInput.send_keys('ghostrecon1')

passwordNext = browser.find_element_by_id('passwordNext')
passwordNext.submit()
