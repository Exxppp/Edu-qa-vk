from ui.pages.base_page import BasePage
from ui.locators.basic_locators import RegisterPageLocators
from builder import Builder


class RegisterPage(BasePage):

    locators = RegisterPageLocators
    url = 'http://localhost:9090/reg'
    builder = Builder()

    def register(self, name=None, surname=None, middlename=None, username=None, email=None, password=None,
                 repeat_password=None, checkbox=True):
        name = name if name else self.builder.user().name
        surname = surname if surname else self.builder.user().surname
        middlename = middlename if middlename else self.builder.user().middle_name
        username = username if username else self.builder.user().username
        email = email if email else self.builder.user().email
        password = password if password else self.builder.user().password
        repeat_password = repeat_password if repeat_password else password

        self.input_text(self.locators.INPUT_NAME, name)
        self.input_text(self.locators.INPUT_SURNAME, surname)
        self.input_text(self.locators.INPUT_MIDDLENAME, middlename)
        self.input_text(self.locators.INPUT_USERNAME, username)
        self.input_text(self.locators.INPUT_EMAIL, email)
        self.input_text(self.locators.INPUT_PASSWORD, password)
        self.input_text(self.locators.INPUT_REPEAT_PASSWORD, repeat_password)
        if checkbox:
            self.click(self.locators.ACCEPT)
        self.click(self.locators.BUTTON_REG)
