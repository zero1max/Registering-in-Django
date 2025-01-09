import requests
from datetime import datetime


def send_msg(*args):
    token = "YOUR_BOT_TOKEN"

    user_id = "YOUR_TG_USER_ID"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {args}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())