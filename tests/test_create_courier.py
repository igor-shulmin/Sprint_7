import allure


class TestCreateCourier:

    @allure.title('Проверка создания аккаунта курьера')
    def test_create_courier(self, new_courier):

        assert len(new_courier.register_new_courier_and_return_login_password()) == 3
        assert new_courier.response.status_code == 201
        assert new_courier.response.json()["ok"] == True

    @allure.title('Проверка невозможности создания одинаковых аккаунтов курьера')
    def test_create_two_same_courier_error(self, new_courier):
        login, password, first_name = new_courier.register_new_courier_and_return_login_password()
        new_courier.register_new_courier_with_data(login, password, first_name)

        assert new_courier.response.status_code == 409

    @allure.title('Проверка невозможности создания аккаунта курьера без заполнения обязательного поля')
    def test_create_courier_without_required_field_error(self, new_courier):
        password = new_courier.generate_random_string()
        first_name = new_courier.generate_random_string()
        new_courier.register_new_courier_with_data(login=None, password=password, first_name=first_name)

        assert new_courier.response.status_code == 400
