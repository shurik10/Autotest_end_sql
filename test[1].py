# Александр Арчаков, когорта 8а — Финальный проект. Инженер по тестированию плюс
import requests
# Импортируем библиотеку requests
from config import adres_servera, dannyye_zakaza, info_treka, url_zakazazat
# Импотрируем необходимые наборы данных из файла config


def test_sozdaniye_zakaza_i_proverka_otveta():
    # Создаём заказ
    url_sozdat = adres_servera + url_zakazazat
    telo_sozdat = requests.post(url_sozdat, json=dannyye_zakaza)

    # Сохраняем трек-номер заказа
    nomer_zakaza = telo_sozdat.json()["track"]

    # Получаем информацию о заказе по его трек-номеру
    url_poluchit = adres_servera + info_treka + str(nomer_zakaza)
    polucheniye_otveta = requests.get(url_poluchit)

    # Проверяем, что код ответа равен 200
    assert polucheniye_otveta.status_code == 200
