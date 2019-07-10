import requests
import re
from requests.exceptions import RequestException
from multiprocessing import Pool
import json

def get_one_page(url):
    try:
        headers = {
            'Host': 'maoyan.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Cache - Control': 'no - cache'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

def parse_one_page(html):
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
    # +'.*?>(.*?)</a>.*?start">(.*?)</p>.*?releasetime">(.*?)</p>'
    # +'.*?interger">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    pattern = re.compile('<dd>.*?board-index.*?>(\d*)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a'
                         + '>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?).*?fraction">(.*?)</i></p>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield{
            '排名': item[0],
            '电影名称': item[2],
            '海报预览': item[1],
            '演员': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '国别': item[4].strip()[16:18],
            '得分': item[5] + item[6]
        }

def write_to_file(content):
    with open("result.txt", 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")
        f.close()

def main(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

def main_pre():
    url = "http://maoyan.com/board/4?"
    html = get_one_page(url)
    pattern = re.compile('<dd>.*?board-index.*?>(\d*)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a'
                         + '>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?).*?fraction">(.*?)</i></p>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        print(item)


if __name__ == '__main__':
    #main_pre()
    #  main(10)

    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])

