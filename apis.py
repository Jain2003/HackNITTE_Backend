import requests



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

