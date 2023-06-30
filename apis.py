import requests
import urllib
import base64
import time
from sqlOperations import get_native_contest_details


def get_contests():
    try:
        result = {}
        req = requests.get("https://kontests.net/api/v1/codeforces")
        temp = req.json()
        result["codeforces"] = temp
        req = requests.get("https://kontests.net/api/v1/code_chef")
        temp = req.json()
        result["codechef"] = temp
        req = requests.get("https://kontests.net/api/v1/leet_code")
        temp = req.json()
        result["leetcode"] = temp
        return result
    except:
        return []


def login():
    payload = {"username": "Harrish_7", "password": "Mharrish@7"}
    req1 = requests.post("https://vjudge.net/user/login", data=payload)
    return req1

cookies = None

def submit_code(code,lang,prob):
    global cookies
    t = urllib.parse.quote(code)
    encode = base64.b64encode(t.encode())
    print(encode)
    res = get_native_contest_details()
    contest = res[0][2]
    if cookies is None:
        cookies = login()

    payload2 = {"method": 0, "language": int(lang), "open": 0, "source": encode, "captcha": "", "password": ""}

    req2 = requests.post(f"https://vjudge.net/contest/submit/{contest}/{prob}", data=payload2, cookies=cookies.cookies)

    print(req2.text)

    t2 = req2.json()
    if 'runId' not in t2:
        cookies = login()
        print("extra Logged In")
        req2 = requests.post(f"https://vjudge.net/contest/submit/{contest}/{prob}", data=payload2,
                             cookies=cookies.cookies)
        t2 = req2.json()
    print(t2)
    verdict = "PENDING"
    while verdict == "PENDING":
        req3 = requests.post(f"https://vjudge.net/solution/data/{t2['runId']}")
        verdict = req3.json()['statusCanonical']
        time.sleep(1)
    return verdict

