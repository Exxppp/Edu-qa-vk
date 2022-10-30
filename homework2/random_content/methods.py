import random
import string


def random_text(max_len=10):
    return ''.join([random.choice(string.ascii_letters) for i in range(max_len)])
