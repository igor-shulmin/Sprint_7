import allure


class TestGetOrderByNum:

    @allure.title('Проверка возврата заказа при указании трек-номера в запросе')
    def test_get_order_by_num(self, new_order):
        new_order.get_order_id()

        assert new_order.response.status_code == 200
        assert bool(new_order.response.json().get("order")) == True

    @allure.title('Проверка невозможности возврата заказа при отсутствии трек-номера в запросе')
    def test_get_order_without_num_error(self, new_order):
        new_order.get_order_with_data()

        assert new_order.response.status_code == 400

    @allure.title('Проверка невозможности возврата заказа при некорректном трек-номере в запросе')
    def test_get_order_by_uncorrect_num_error(self, new_order):
        new_order.get_order_with_data(track_num=00000)

        assert new_order.response.status_code == 404
