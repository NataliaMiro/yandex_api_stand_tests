import sender_stand_request
import data

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body



# Функция для позитивной проверки
def positive_assert(name):
    # В переменную name сохраняется обновлённое тело запроса:
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    # В переменную kit_responce сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа = 201
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] ==name

    # Функция для негативной проверки
def negative_assert(name):
    # В переменную name сохраняется обновлённое тело запроса:
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    #  Проверяется, что код ответа = 400
    assert kit_response.status_code == 400


# Тест 1. Допустимое количество символов.
#  Параметр name состоит из 1 символа
def test_create_kit_1_letter_name_get_success_response():
    positive_assert("a")

