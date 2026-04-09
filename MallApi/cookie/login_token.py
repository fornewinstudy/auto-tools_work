import requests
import pymysql

def toke():
    loin_url = "http://appapi.fecshop.com/v1/account/login"
    loin_json = {
        "username": "admin",
        "password": "admin123"
    }
    loin_requ = requests.post(url=loin_url, json=loin_json).json()
    # assert "success" in loin_requ.values()
    header = {'access-token': loin_requ.get('access-token')}
    print(header)
    return header

if __name__ == '__main__':
    toke()