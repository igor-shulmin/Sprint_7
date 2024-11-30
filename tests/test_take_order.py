import allure


class TestTakeOrder:

    @allure.title('Проверка принятия курьером заказа')
    def test_take_order(self, courier_order):
        courier_order.courier_take_order()

        assert courier_order.response.status_code == 200
        assert courier_order.response.json()["ok"] == True

    @allure.title('Проверка невозможности принять заказ, если он в работе')
    def test_take_order_in_progress_error(self, courier_order):
        order_id = courier_order.courier_take_order()
        courier_id = courier_order.login_courier_and_return_courier_id()
        courier_order.courier_take_order_with_data(order_id=order_id, courier_id=courier_id)

        assert courier_order.response.status_code == 409

    @allure.title('Проверка невозможности принять заказ при некорректном ID курьера')
    def test_take_order_uncorrect_courier_id_error(self, courier_order):
        order_id = courier_order.get_order_id()
        courier_order.courier_take_order_with_data(order_id=order_id, courier_id=1000000)

        assert courier_order.response.status_code == 404

    @allure.title('Проверка невозможности принять заказ при некорректном ID заказа')
    def test_take_order_uncorrect_order_id_error(self, courier_order):
        courier_id = courier_order.login_courier_and_return_courier_id()
        courier_order.courier_take_order_with_data(order_id=1000000, courier_id=courier_id)

        assert courier_order.response.status_code == 404

    @allure.title('Проверка невозможности принять заказ при отсутствии ID курьера')
    def test_take_order_without_courier_id_error(self, courier_order):
        order_id = courier_order.get_order_id()
        courier_order.courier_take_order_with_data(order_id=order_id)

        assert courier_order.response.status_code == 400

    @allure.title('Проверка невозможности принять заказ при отсутствии ID заказа')
    def test_take_order_without_order_id_error(self, courier_order):
        courier_id = courier_order.login_courier_and_return_courier_id()
        courier_order.courier_take_order_with_data(courier_id=courier_id)

        assert courier_order.response.status_code == 400
