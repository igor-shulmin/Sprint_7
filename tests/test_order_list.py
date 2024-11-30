import allure


class TestOrderList:

    @allure.title('Проверка возврата списка заказов по ID курьера')
    def test_check_order_list(self, new_courier):
        new_courier.get_order_list_by_courier_id()

        assert new_courier.response.status_code == 200
        assert type(new_courier.response.json().get("orders")) == list
        assert len(new_courier.response.json().get("orders")) == 0
