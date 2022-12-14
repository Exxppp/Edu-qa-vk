import faker

fake = faker.Faker()


def generate_str(length=None):
    if length is None:
        length = fake.pyint(min_value=6, max_value=16)
    new_str = fake.lexify('?' * length)

    return new_str


def generate_unique_str(length=None):
    if length is None:
        length = fake.pyint(min_value=6, max_value=16)
    new_str = fake.unique.lexify('?' * length)

    return new_str


def generate_email():
    return fake.unique.email()

