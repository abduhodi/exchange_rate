import requests
import flag

def getrate():
    url = "https://nbu.uz/uz/exchange-rates/json/"
    response = requests.get(url)
    jsondata = response.json()

    data = f"Valyuta nomi{flag.flag('US')}: {jsondata[23]['title']}\
           \nSotib olish: {jsondata[23]['nbu_buy_price']}  so`m\
           \nSotish: {jsondata[23]['nbu_cell_price']}  so`m\
           \n\nValyuta nomi{flag.flag('RU')}: {jsondata[18]['title']}\
           \nSotib olish: {jsondata[18]['nbu_buy_price']}  so`m\
           \nSotish: {jsondata[18]['nbu_cell_price']}  so`m\
           \n\nValyuta nomi{flag.flag('EU')}: {jsondata[7]['title']}\
           \nSotib olish: {jsondata[7]['nbu_buy_price']}  so`m\
           \nSotish: {jsondata[7]['nbu_cell_price']}  so`m\
           \n\nValyuta nomi{flag.flag('TR')}: {jsondata[21]['title']}\
           \nSotib olish: {jsondata[21]['nbu_buy_price']}  so`m\
           \nSotish: {jsondata[21]['nbu_cell_price']}  so`m\
           \n\n So`nggi yangilanish: {jsondata[0]['date']}"

    return data
