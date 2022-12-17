import time

import faker
import requests

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


def wait_ready(host, port, wait_time=820):
    started = False
    st = time.time()
    while time.time() - st <= wait_time:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except:
            pass

    if not started:
        raise RuntimeError(f'App did not started in {wait_time}s!')
