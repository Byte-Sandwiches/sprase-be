import requests
from os import environ

class WS:
    def __init__(self) -> None:
        self.__api_url = environ.get("RT_URL")
        self.__api_key = environ.get("RT_KEY")

    def publish(self, chan: str, payload: dict):
        try:
            data = {
                "method": "publish",
                "params": {
                    "channel": chan,
                    "data": payload
                }
            }

            res = requests.post(
                url=self.__api_url,
                data=data,
                headers={
                    "Authorization": self.__api_key,
                    "Content-Type": "application/json"
                }
            )

            print(res.json())
            # logger
        except Exception as e:
            print(e)

ws = WS()
