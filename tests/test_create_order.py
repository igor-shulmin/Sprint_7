import pytest
import allure


class TestCreateOrder:

    @allure.title('Проверка создания заказа х 4 варианта цвета')
    @pytest.mark.parametrize("color", [["BLACK"], ["GRAY"], ["BLACK", "GRAY"], []])
    def test_create_order(self, new_order, color):
        new_order.create_new_order(color)

        assert new_order.response.status_code == 201
        assert bool(new_order.response.json().get("track")) == True
