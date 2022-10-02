from selenium.webdriver.common.by import By


def auth(browser, email='testgdhdhsjsjs@gmail.com', password='123456q'):
    browser.get('https://target-sandbox.my.com/')
    element = browser.find_element(By.CSS_SELECTOR, '.responseHead-module-button-2yl51i')
    element.click()
    element = browser.find_element(By.NAME, 'email')
    element.clear()
    element.send_keys(email)
    element = browser.find_element(By.NAME, 'password')
    element.clear()
    element.send_keys(password)
    element = browser.find_element(By.CLASS_NAME, 'authForm-module-button-1u2DYF')
    element.click()
