import requests
from bs4 import BeautifulSoup


list_proxies = []
site_link = "https://www.proxynova.com/proxy-server-list"


def parsing():
    r = requests.get(site_link).text
    site = BeautifulSoup(r, features="html.parser")
    list_trs = site.find_all("tbody")[0].find_all("tr")

    for tr in list_trs:
        try:
            ip = str(tr.find("abbr").contents[1]).strip("</script> document.write('');").replace("' + '", "")
            port = tr.find_all("td")[1].text.strip()
            list_proxies.append(f"{ip}:{port}")
        except Exception as e:
            pass

    return list_proxies
