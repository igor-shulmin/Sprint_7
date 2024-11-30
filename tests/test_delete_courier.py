import allure


class TestDeleteCourier:

    @allure.title('Проверка удаления аккаунта курьера')
    def test_delete_courier(self, new_courier):
        new_courier.delete_courier_by_courier_id()

        assert new_courier.response.status_code == 200
        assert new_courier.response.json()["ok"] == True

    @allure.title('Проверка невозможности удаления аккаунта курьера при отсутствии ID в запросе')
    def test_delete_courier_without_id_error(self, new_courier):
        new_courier.delete_courier_with_data()

        assert new_courier.response.status_code == 400

    @allure.title('Проверка невозможности удаления аккаунта курьера при некорректном ID в запросе')
    def test_delete_courier_with_uncorrect_id_error(self, new_courier):
        new_courier.delete_courier_with_data(id=000)

        assert new_courier.response.status_code == 404
