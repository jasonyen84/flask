import requests
from bs4 import BeautifulSoup


def crawl_stocks():
    url = "https://histock.tw/%E5%9C%8B%E9%9A%9B%E8%82%A1%E5%B8%82"
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "lxml")
        trs = soup.find(string="加權指數").find_parent("div").find_all("tr")

        datas = []
        for tr in trs:
            data = []
            for th in tr.find_all("th"):

                data.append(th.text.strip())

            for td in tr.find_all("td"):

                data.append(td.text.strip())
            datas.append(data)

        return datas
    except Exception as e:
        print(e)
    return None


def crawl_pm25():
    url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
    try:
        datas = requests.get(url).json()["records"]
        columns = list(datas[0].keys())
        values = [list(data.values()) for data in datas]

        return columns, values

    except Exception as e:
        print(e)
    return None, 404


if __name__ == "__main__":
    pass
