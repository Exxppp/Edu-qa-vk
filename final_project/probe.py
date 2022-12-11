import requests
from faker import Faker


fake = Faker()
#
# test2 = ApiClient()
# a = test2.create_user_reg()


# host, port = VK_URL.split(':')
# print(host)
# print(port)
def generate(length):
    name = fake.unique.lexify('?'*length+'#####')
    return name


print(generate(23))
