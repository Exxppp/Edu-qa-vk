from ui.locators import basic_locators


def auth(browser, email='testgdhdhsjsjs@gmail.com', password='123456q'):
    browser.get('https://target-sandbox.my.com/')
    element = browser.find_element(*basic_locators.LOG_IN_BUTTON)
    element.click()
    element = browser.find_element(*basic_locators.INPUT_EMAIL)
    element.clear()
    element.send_keys(email)
    element = browser.find_element(*basic_locators.INPUT_PASSWORD)
    element.clear()
    element.send_keys(password)
    element = browser.find_element(*basic_locators.LOG_IN_BUTTON_AUTH_FORM)
    element.click()
