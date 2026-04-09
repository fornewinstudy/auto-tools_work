import requests
import random
import re
from MallApi.cookie.cookies import lion_cookie

def query(fruits=random.randint(1,53)):
    query_url = "http://www.mall.com/search.php?"
    query_date = {
        "keywords": f"{fruits}",
        "dataBi":"k1"
    }
    cookie = lion_cookie()
    query_est = requests.post(url=query_url, data=query_date,cookies=cookie)
    tmp = re.findall(r'"goods\.php\?id=(\d+)"',query_est.text)
    am = random.choice(tmp)
    print(am)
    return am

if __name__ == '__main__':
    query()
