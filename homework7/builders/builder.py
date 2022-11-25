from faker import Faker

fake = Faker()


class Builder:

    @staticmethod
    def generate_name():
        return fake.unique.first_name()

    @staticmethod
    def generate_surname():
        return fake.unique.last_name()
