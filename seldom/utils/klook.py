"""
The @KLOOK Company API
"""
import requests
from requests.exceptions import RetryError
from seldom.logging import log


class Lark:
    """send lark message class"""

    def __init__(self, url: str, app_id: str):
        self.url = url
        self.headers = {'App': app_id}

    @staticmethod
    def get_card_message(url: str, title: str, desc: str) -> dict:
        """
        Send message template
        :return:
        """
        message = {
            "card_link": {
                "url": url
            },
            "config": {
                "wide_screen_mode": True
            },
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": title
                }
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"{desc}"
                    }
                }
            ]
        }
        return message

    def send_card_message(self,
                          message: dict,
                          chat_id: str = None,
                          open_id: str = None,
                          user_id: str = None,
                          email: str = None) -> dict:
        """
        send card to user
        :param message:
        :param chat_id:
        :param open_id:
        :param user_id:
        :param email:
        :return:
        """
        if (chat_id is None) and (open_id is None) and (user_id is None) and (email is None):
            raise ValueError("Please specify what to send: chat_id/open_id/user_id/email.")

        req_body = {"msg_type": "interactive", "card": message}
        if chat_id is not None:
            req_body["chat_id"] = chat_id
        if open_id is not None:
            req_body["open_id"] = open_id
        if user_id is not None:
            req_body["user_id"] = user_id
        if email is not None:
            req_body["email"] = email

        try:
            r = requests.post(url=self.url, headers=self.headers, json=req_body)
            if r.status_code == 200:
                error = r.json().get('error', {})
                code = error.get('code', -1)
                if code == '0':
                    log.success(f'[message] success, {r.json()}')
                    return r.json()
                log.error(f'[message] got error, {r.text}')
                return {}
            log.error(f'[message] got error, {r.text}')
            return {}
        except RetryError as e:
            log.error(f'[message] got retry error, error: {e}')
            return {}
        except Exception as e:
            log.error(f'[message] got exception error, error: {e}')
            return {}


class MockEnv:
    """
    修改请求指向Mock环境
    """

    def __init__(self, url: str, data: dict = None, json: dict = None, **kwargs):
        self.url = url
        self.data = data
        self.json = json
        self.kwargs = kwargs

    def update(self) -> dict:
        """update mock env"""
        try:
            r = requests.post(url=self.url, data=self.data, json=self.json, **self.kwargs)
            if r.status_code == 200:
                success = r.json().get('success')
                if success is True:
                    log.success(f'[mock] success, {r.json()}')
                    return r.json()
                log.error(f'[mock] got error, {r.text}')
                return {}
            log.error(f'[message] got error, {r.text}')
            return {}
        except RetryError as e:
            log.error(f'[mock] got retry error, error: {e}')
            return {}
        except Exception as e:
            log.error(f'[mock] got exception error, error: {e}')
            return {}
