import allure
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import ApiClient

BASE_URL = "https://petstore.swagger.io"
pet_id = 7
pet_name = "Lions"
new_pet_id = 77
new_pet_name = "Lucky"
del_pet_id = 5

@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)

@allure.feature("[api test] Создание питомца")
@allure.story("Позитивный тест")
def test_create_pet(api_client):
    with allure.step("Тело запроса на создание питомца"):
     data = {
        "id": pet_id,
        "name": pet_name,
        "photoUrls": ["http://example.com/photo.jpg"],
        "status": "available"
     }

    with allure.step("Отправить POST запрос"):
     response = api_client.post("/v2/pet", data=data)

    with allure.step("Проверка ответа"):
     assert response.status_code == 200
     assert response.json()["name"] == pet_name


@allure.feature("[api test] Получение питомца по его id")
@allure.story("Позитивный тест")
def test_get_pet(api_client):
    with allure.step("Отправить GET запрос"):
     response = api_client.get(f"/v2/pet/{pet_id}")

    with allure.step("Проверка ответа"):
     assert response.status_code == 200
     assert response.json()["id"] == pet_id


@allure.feature("[api test] Обновить данные питомца")
@allure.story("Позитивный тест")
def test_upd_pet(api_client):
    with allure.step("Обновленные данные питомца"):
     data = {
        "id": new_pet_id,
        "name": new_pet_name,
        "status": "available"
    }

    with allure.step("Отправить PUT запрос"):
     response = api_client.put("/v2/pet", data=data)
    with allure.step("Проверка ответа"):
     assert response.status_code == 200
     assert response.json()["name"] == new_pet_name

@allure.feature("[api test] Удалить питомца")
@allure.story("Позитивный тест")
def test_delete_pet(api_client):
    with allure.step("Отправить DELETE запрос"):
     response = api_client.delete(f"/v2/pet/{del_pet_id}")

     with allure.step("Проверка ответа"):
      assert response.status_code == 200

@allure.feature("[api test] Получение питомца по его id")
@allure.story("Негативный тест")
def test_get_pet_negative(api_client):
    with allure.step("Отправить GET запрос"):
     response = api_client.get("/v2/pet/99999599")

    with allure.step("Проверка ответа"):
     assert response.status_code == 404