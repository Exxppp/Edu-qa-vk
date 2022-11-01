from dataclasses import dataclass
import faker

faker = faker.Faker()


class Builder:
    @staticmethod
    def ad(name=None, text=None, title=None, price=None):
        @dataclass
        class Company:
            name: str
            title: str
            text: str
            price: str

        if price is None:
            price = faker.pyfloat(1, 2, True, 1)

        if name is None:
            name = faker.lexify('???????')

        if title is None:
            title = faker.lexify('???????????')

        if text is None:
            text = faker.bothify('?? ?#?? ?##????##? ??#? ?????? ??????? ????')

        return Company(name=name, title=title, text=text, price=price)

    @staticmethod
    def segments(name=None):
        @dataclass
        class SegmentInAudience:
            name: str

        if name is None:
            name = faker.lexify('?????????')

        return SegmentInAudience(name=name)
