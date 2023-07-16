import requests as req
from bs4 import BeautifulSoup as bs


def scraprating(cc, cf, lc):
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
    
def scraprecent_usercontest(cc, cf):
    scraprecent=[]
    buffer = ["","","0"]
    if cc != "":
        ccscrap = []
        requests = req.get(f"https://www.codechef.com/users/{cc}")
        soup = bs(requests.content, 'html.parser')
        box = soup.find(attrs= {'id':"rating-box-all" })
        contestname = box.find('div', class_='contest-name')
        links = box.find('a')
        if links:
            contest_name = links.get_text() 
            contestlink = links['href'] if 'href' in links.attrs else None
            globalrank = box.find('strong', class_ = 'global-rank')
            rank = globalrank.get_text()
            ccscrap.append(contest_name)
            ccscrap.append(contestlink)
            ccscrap.append(rank)
        if ccscrap:
            scraprecent.append(ccscrap)
        else:
            scraprecent.append(buffer)
    if cf != "":
        cfscrap = []
        requests = req.get(f"https://codeforces.com/contests/with/{cf}")
        soup = bs(requests.content, 'html.parser')
        tables = soup.find('table', class_='tablesorter user-contests-table')
        onlyvalues = tables.find('tbody')
        firstrow = onlyvalues.find('tr')
        tabcontent = []
        values = firstrow.find_all('td')
        for value in values:
            tabcontent.append(value)

        link = tabcontent[1]
        links = link.find('a')
        if links:
            contest_name = links.get_text()
            contest_name = contest_name.replace("\r", "")
            contest_name = contest_name.replace("\n", "")
            contest_name = contest_name.replace("                    ", "")
            contest_link = links['href'] if 'href' in links.attrs else None
            contestlink = "https://codeforces.com" + contest_link
        
        rank = tabcontent[3].get_text()
        cfscrap.append(contest_name)
        cfscrap.append(contestlink)
        cfscrap.append(rank)
        if cfscrap:
            scraprecent.append(cfscrap)
        else:
            scraprecent.append(buffer)

    if not scraprecent:
        return "NO UserName Found or Error"
    else:
        return scraprecent

