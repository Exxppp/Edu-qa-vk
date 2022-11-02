from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOG_IN_BUTTON = (By.XPATH, "//div[contains(@class,'Head-module-button')]")
    INPUT_EMAIL = (By.XPATH, "//input[@name='email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOG_IN_BUTTON_AUTH_FORM = (By.XPATH, "//div[contains(@class,'authForm-module-button')]")


class DashboardPageLocators:
    CREATE_NEW_COMPANY = (By.XPATH, "//div[contains(@class,'blue')]")
    VK_PRODUCTS = (By.XPATH, "//div[contains(@class,'general_ttm')]")
    LINK = (By.XPATH, "//input[contains(@data-gtm-id,'url')]")
    AD_PRODUCT_90X75 = (By.XPATH, "//div[contains(text(),'90')]")
    UPLOAD_CREATIVE = (By.XPATH, "//input[@data-test='image_90x75']")
    SAVE_AD = (By.XPATH, "//div[@data-test='submit_banner_button']")
    TITLE_AD = (By.XPATH, "//input[@data-name='title_25']")
    TEXT_AD = (By.XPATH, "//textarea[@data-name='text_90']")
    SAVE_COMPANY = (By.XPATH, "//button[@data-service-readonly='true']")
    NAME_COMPANY = (By.XPATH, "//input[@data-dictionary-attr-path and (@maxlength)]")
    GET_NAME_COMPANY = (By.XPATH, "//a[contains(@class,'nameCell')]")
    ACTIONS = (By.XPATH, "//div[contains(@class,'mass')]")
    SELECT_COMPANY = (By.XPATH, "//div[contains(@class,'nameCell')]/input")
    SELECT_ALL_COMPANY = (By.XPATH, "//div[contains(@class,'Wrap')]/input")
    DELETE = (By.XPATH, "//li[@data-test='8']")
    COUNT_COMPANY = (By.XPATH, "//div[contains(@class,'campaign')]")


class SegmentsPageLocators:
    SEGMENT_LIST = (By.XPATH, "//a[@href='/segments/segments_list']")
    CREATE_NEW_SEGMENT = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    APPS_AND_GAMES = (By.XPATH, "//div[text()='Приложения и игры в соцсетях']")
    PLAYED_AND_PAID_IN_PLATFORM = (By.XPATH, "//span[@class='js-source-name']")
    PLAYED_IN_PLATFORM = (By.XPATH, "//input[contains(@class,'play')]")
    BUTTON_ADD_SEGMENT = (By.XPATH, "//div[contains(@class,'add-button')]/button")
    BUTTON_CREATE_SEGMENT = (By.XPATH, "//button[@class='button button_submit']")
    NAME_SEGMENT = (By.XPATH, "//div[@class='js-segment-name']//input")
    NAME_SEGMENT_IN_LIST = (By.XPATH, "//a[@title]")
    SELECT_SEGMENT = (By.XPATH, "//div[contains(@class,'idCellWrap')]/input")
    ACTIONS = (By.XPATH, "//div[contains(@class,'mass')]")
    REMOVE_SEGMENTS = (By.XPATH, "//li[contains(@data-test,'remove')]")
    GROUPS_VK_AND_OK = (By.XPATH, "//a[@href='/segments/groups_list']")
    INPUT_LINK_GROUPS_VK_AND_OK = (By.XPATH, "//input[contains(@class,'Suggester')]")
    SELECT_ALL = (By.XPATH, "//div[@data-test='select_all']")
    ADD_SELECTED = (By.XPATH, "//div[@data-test='add_selected_items_button']")
    DATA_SOURCE_VK = (By.XPATH, "//tr[@class='flexi-table__row']")
    REMOVE_DATA_SOURCE_VK = (By.XPATH, "//td[contains(@class,'cell-remove')]")
    CONFIRM_REMOVE = (By.XPATH, "//button[contains(@class, 'remove')]")
    SEGMENT_VK_AND_OK = (By.XPATH, "//div[text()='Группы ОК и VK']")
    SELECT_GROUP_VK = (By.XPATH, "//input[contains(@class,'adding')]")
    COUNT_SEGMENTS = (By.XPATH, "//div[contains(@data-test,'name')]")
