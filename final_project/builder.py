from copy import copy
from dataclasses import dataclass

import faker

fake = faker.Faker()


class Builder:
    @staticmethod
    def user(name=None, surname=None, middle_name=None, username=None, password=None, email=None):
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
            name = fake.unique.first_name()

        if surname is None:
            surname = fake.unique.last_name()

        if middle_name is False:
            middle_name = ''
        elif middle_name is None:
            middle_name = fake.unique.lexify('???????')

        if username is None:
            username = fake.unique.pystr(min_chars=6, max_chars=15)

        if password is None:
            password = fake.unique.lexify('???????')

        if email is None:
            email = fake.unique.email()

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
