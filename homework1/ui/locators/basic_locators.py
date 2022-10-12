from selenium.webdriver.common.by import By


HTML = (By.CSS_SELECTOR, 'html')

LOG_IN_BUTTON = (By.XPATH, "//div[starts-with(@class,'responseHead-module-button')]")
INPUT_EMAIL = (By.XPATH, "//input[@name='email']")
INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
LOG_IN_BUTTON_AUTH_FORM = (By.XPATH, "//div[starts-with(@class,'authForm-module-button')]")

EDIT_INF_INPUT_1 = (By.XPATH, "(//input)[1]")
EDIT_INF_INPUT_2 = (By.XPATH, "(//input)[2]")
EDIT_INF_INPUT_3 = (By.XPATH, "(//input)[3]")
EDIT_INF_BUTTON = (By.XPATH, "//button")
EDIT_INF_SUCCESS = (By.XPATH, "//div[contains(@class, 'js-group-form-success-bg')]")

ELEMENTS_ON_HEADERS = (By.XPATH, "//li[starts-with(@class,'center-module-buttonWrap')]")
DASHBOARD = (By.XPATH, "//li[starts-with(@class, 'instruction-module-item')][4]")
SEGMENTS = (By.XPATH, "//div[contains(@class,'page_segments_segmentslist')]")
BILLING = (By.XPATH, "//body[contains(@class,'current-page_billing')]")
STATISTICS = (By.XPATH, "//div[contains(@class,'page_statistics_summary_nt')]")
PRO = (By.XPATH, "//body[contains(@class,'current-page_no-type')]")
PROFILE = (By.XPATH, "//div[contains(@class,'page_profile')]")
TOOLS = (By.XPATH, "//div[contains(@class,'page_tools')]")
HELP = (By.XPATH, "//div[@id='allrecords']")

LOG_OUT_BUTTON = (By.XPATH, "//div[starts-with(@class,'right-module-rightButton')]")
LOG_OUT_BUTTON_CLICK = (By.XPATH, "//li[starts-with(@class,'rightMenu-module-rightMenuItem')][2]")

NOTIFY_AUTH_FORM = (By.XPATH, "//div[starts-with(@class,'notify-module-content')]")
DISABLE_BUTTON = (By.CSS_SELECTOR, '.authForm-module-disabled-104QGH')
