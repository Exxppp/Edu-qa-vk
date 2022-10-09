import time


def wait(browser, selector, method='len', sec=8, length=8):
    times = sec * 5
    if method == 'len':
        for i in range(times):
            if len(browser.find_elements(*selector)) == length:
                return
            else:
                time.sleep(0.2)
    elif method == 'is_displayed':
        for i in range(times):
            element = browser.find_element(*selector)
            if element:
                if element.is_displayed():
                    return
                else:
                    time.sleep(0.2)
            else:
                time.sleep(0.2)
    return
