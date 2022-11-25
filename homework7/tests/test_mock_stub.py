from tests.base import BaseCaseApi


class TestMock(BaseCaseApi):

    def test_add_user(self):
        name = self.builder.generate_name()
        response = self.api_client.create_user_by_name(name)

        assert response['name'] == name

    def test_add_surname(self):
        name = self.builder.generate_name()
        response = self.api_client.create_user_by_name(name)

        assert response['surname']

    def test_get_user_by_name(self):
        name = self.builder.generate_name()
        self.api_client.create_user_by_name(name)

        user = self.api_client.get_user_by_name(name)

        assert user['user_id']
        assert user['surname']

    def test_update_user_surname_by_name(self):
        name = self.builder.generate_name()
        surname = self.builder.generate_surname()

        given_surname = self.api_client.create_user_by_name(name)['surname']
        self.api_client.update_surname_by_name(name, surname)

        user = self.api_client.get_user_by_name(name)

        assert user['surname'] == surname
        assert given_surname != surname

    def test_delete_user_by_name(self):
        name = self.builder.generate_name()
        self.api_client.create_user_by_name(name)

        self.api_client.delete_user_by_name(name)
        response = self.api_client.get_user_by_name(name)

        assert response['surname'] is None
