from selenium.webdriver.common.by import By


class BasePageLocators:

    pass


class LoginPageLocators:
    LOG_IN_BUTTON = (By.XPATH, "//div[starts-with(@class,'responseHead-module-button')]")
    INPUT_EMAIL = (By.XPATH, "//input[@name='email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOG_IN_BUTTON_AUTH_FORM = (By.XPATH, "//div[starts-with(@class,'authForm-module-button')]")


class DashboardPageLocators:
    CREATE_NEW_COMPANY = (By.XPATH, "//div[contains(@class,'dashboard-module-createButtonWrap')]/div/div")
    VK_PRODUCTS = (By.XPATH, "//div[contains(@class,'_general_ttm')]")
    LINK = (By.XPATH, "//div[contains(@class, 'suggester')]//input")
    FIRST_AD_PRODUCT = (By.XPATH, "//div[contains(@class,'column-list-item pac')][1]")
    UPLOAD_CREATIVE = (By.XPATH, "//input[@data-test='image_90x75']")
    SAVE_AD = (By.XPATH, "//div[@data-test='submit_banner_button']")
    TITLE_AD = (By.XPATH, "//input[@data-name='title_25']")
    TEXT_AD = (By.XPATH, "//textarea[@data-name='text_90']")
    SAVE_COMPANY = (By.XPATH, "//div[@class='footer__button js-save-button-wrap']/button")
    NAME_COMPANY = (By.XPATH, "//div[@class='campaign-name']//input")
    GET_NAME_COMPANY = (By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink')]")
    ACTIONS = (By.XPATH, "//div[contains(@class,'tableControls-module-massActionsSelect')]")
    SELECT_ALL_COMPANY = (By.XPATH, "//div[contains(@class,'header-module-noWrap')]/input")
    DELETE = (By.XPATH, "//li[@data-test='8']")


class SegmentsPageLocators:
    CREATE_NEW_SEGMENT = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    APPS_AND_GAMES = (By.XPATH, "//div[text()='Приложения и игры в соцсетях']")
    PLAYED_AND_PAID_IN_PLATFORM = (By.XPATH, "//span[@class='js-source-name']")
    PLAYED_IN_PLATFORM = (By.XPATH, "//input[contains(@class,'js-payer-checkbox-play')]")
    BUTTON_ADD_SEGMENT = (By.XPATH, "//div[contains(@class,'js-add-button')]/button")
    BUTTON_ADD_SEGMENTS = (By.XPATH, "//button[@class='button button_submit']")
    NAME_SEGMENT = (By.XPATH, "//div[@class='js-segment-name']//input")
    NAME_SEGMENT_IN_LIST = (By.XPATH, "//div[contains(@class,'cells-module-nameCell')]/a")
    SELECT_SEGMENT = (By.XPATH, "//div[contains(@class,'segmentsTable-module-idCellWrap')]/input")
    ACTIONS = (By.XPATH, "//div[contains(@class,'segmentsTable-module-massActionsSelect')]")
    REMOVE_SEGMENTS = (By.XPATH, "//li[contains(@data-test,'remove')]")

    GROUPS_VK_AND_OK = (By.XPATH, "//a[@href='/segments/groups_list']")
    INPUT_LINK_GROUPS_VK_AND_OK = (By.XPATH, "//input[contains(@class,'multiSelectSuggester-module-searchInput')]")
    SELECT_ALL = (By.XPATH, "//div[@data-test='select_all']")
    ADD_SELECTED = (By.XPATH, "//div[@data-test='add_selected_items_button']")
    DATA_SOURCE_VK = (By.XPATH, "//tr[@class='flexi-table__row']")
    REMOVE_DATA_SOURCE_VK = (By.XPATH, "//a[@href='https://vk.com/vkedu']/../../td/div/div")
    CONFIRM_REMOVE = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")
