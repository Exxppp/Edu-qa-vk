from appium.webdriver.common.mobileby import MobileBy


class BasePageANDROIDLocators:
    pass


class MainPageANDROIDLocators(BasePageANDROIDLocators):
    KEYBOARD = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    INPUT_TEXT = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    SEND_TEXT = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_send')
    GET_TITLE = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_title')
    GET_DESCRIPTION_COUNTRY = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_content_text')
    SCROLL_EL = (MobileBy.XPATH, '//android.view.ViewGroup[5]/android.widget.TextView')
    POPULATION_OF_RUSSIA = (MobileBy.XPATH, '//android.view.ViewGroup[4]/android.widget.TextView')
    EXPRESSION_RESULT = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.TextView')
    SETTINGS = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')
    PLAY_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/play_button')
    PLAYER_NAME = (MobileBy.ID, 'ru.mail.search.electroscope:id/player_track_name')
    SEARCH_EL_IN_DOWN_PANEL = (MobileBy.XPATH, '//android.view.ViewGroup/android.widget.TextView')


class PermissionPageANDROIDLocators(BasePageANDROIDLocators):
    ADD_PERMISSION = (MobileBy.XPATH, '//android.widget.Button[1]')


class SettingsPageANDROIDLocators(BasePageANDROIDLocators):
    NEWS_SOURCE = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    CLOSE_SETTINGS = (MobileBy.XPATH, '(//android.widget.ImageButton)[1]')
    ABOUT = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')


class InfoPageANDROIDLocators(BasePageANDROIDLocators):
    VERSION = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_version')
    COPYRIGHT = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_copyright')


class NewsSourcePageANDROIDLocators(BasePageANDROIDLocators):
    MAIL_RU = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    MAIL_RU_SELECTED = (MobileBy.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')
    BACK_BUTTON = (MobileBy.XPATH, '//android.widget.ImageButton')
