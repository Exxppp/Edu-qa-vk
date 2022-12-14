from copy import copy
from dataclasses import dataclass
from utils.func import *


class Builder:

    @staticmethod
    def user(name=None, name_length=None, surname=None, surname_length=None, middle_name=None, middle_name_length=None,
             username=None, username_length=None, password=None, password_length=None, email=None):
        @dataclass
        class User:
            name: str
            surname: str
            middle_name: str
            username: str
            password: str
            email: str
            data: dict
            data_reg: dict

        if name is None:
            name = generate_str(name_length)

        if surname is None:
            surname = generate_str(surname_length)

        if middle_name is None:
            middle_name = generate_str(middle_name_length)

        if username is None:
            username = generate_unique_str(username_length)

        if password is None:
            password = generate_str(password_length)

        if email is None:
            email = generate_email()

        data = {
            "name": name,
            "surname": surname,
            "middle_name": middle_name,
            "username": username,
            "password": password,
            "email": email
        }
        data_reg = copy(data)
        data_reg.update({
            'middlename': middle_name,
            'confirm': password,
            'term': 'y',
            'submit': 'Register'
        })

        return User(name=name, surname=surname, middle_name=middle_name, username=username,
                    password=password, email=email, data=data, data_reg=data_reg)
