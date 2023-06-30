import requests as req
from bs4 import BeautifulSoup as bs


def scrap(cc, cf, lc):
    Rating = []
    if cc != "":
        r = req.get(f"https://www.codechef.com/users/{cc}")
        soup = bs(r.content, 'html5lib')
        rating = soup.find("div", attrs={'class', 'rating-number'})
        Rating.append(rating.text)
    else:
        Rating.append('0')

    if cf != "":
        res = req.get(f'https://codeforces.com/api/user.info?handles={cf}')
        res = res.json()
        rating = str(res["result"][0]["rating"])
        Rating.append(rating)
    else:
        Rating.append("0")

    if lc != "":
        r = req.get(f"https://leetcode.com/{lc}/")
        soup = bs(r.content, 'html5lib')
        rating = soup.find("div", attrs={'class', 'text-label-1 dark:text-dark-label-1 flex items-center text-2xl'})
        Rating.append(rating.text.replace(",", ""))
    else:
        Rating.append('0')


    if not Rating:
        return "NO UserName Found or Error"
    else:
        return Rating

