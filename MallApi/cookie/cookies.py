import requests
from MallApi.conf.config import lion_url

def lion_cookie(name = "abcde",pwod = "123456"):
    url = lion_url
    lion_data = {
        "username": name,
        "password": pwod,
        "act": "act_login",
        "back_act": "./index.php",
        "submit": "登 录"
    }
    req = requests.post(url=url,data=lion_data)
    assert "登录成功" in req.text
    return req.cookies
if __name__ == '__main__':
    print(lion_cookie())
