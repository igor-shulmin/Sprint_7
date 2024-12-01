import allure


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера')
    def test_login_courier(self, new_courier):
        new_courier.login_courier_and_return_courier_id()

        assert new_courier.response.status_code == 200
        assert bool(new_courier.response.json().get("id")) == True

    @allure.title('Проверка невозможности авторизации курьера при некорректных данных')
    def test_login_courier_uncorrect_login_error(self, new_courier):
        login, password, first_name = new_courier.register_new_courier_and_return_login_password()
        new_courier.login_courier_with_data(login=login[:-1], password=password)

        assert new_courier.response.status_code == 404
        assert new_courier.response.json()["message"] == "Учетная запись не найдена"
        assert bool(new_courier.response.json().get("id")) == False

    @allure.title('Проверка невозможности авторизации курьера при незаполненном обязательном поле')
    def test_login_courier_empty_field_error(self, new_courier):
        login, password, first_name = new_courier.register_new_courier_and_return_login_password()
        new_courier.login_courier_with_data(login=login, password="")

        assert new_courier.response.status_code == 400
        assert new_courier.response.json()["message"] == "Недостаточно данных для входа"
        assert bool(new_courier.response.json().get("id")) == False
