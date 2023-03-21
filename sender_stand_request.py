import requests
import configuration
import data


# Создаётся новый пользователь
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, #подставляем полный URL
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


#  Создаётся новый набор с authToken созданного пользователя
def post_new_client_kit(kit_body, auth_token):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=auth_headers)





