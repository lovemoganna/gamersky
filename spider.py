import json
import re

import requests
from requests.exceptions import RequestException


# 1. 获取url,需要加一层异常处理
# requests官方文档: http://docs.python-requests.org/en/master/
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 4.解析一个页面
def parse_onde_page(html):
    pattern = re.compile(
        '<dd.*?movie-item.*?movie-poster.*?<img\ssrc="(.*?)".*?movie-item-title.*?'
        + '<a.*?data-val="(.*?)">(.*?)</a>.*?channel-detail-orange.*?integer">(.*?)</i>' +
        '.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    for item in items:
            yield {'haibao': r[0], 'movieId': r[1], 'movieTitle': r[2], 'Alexa': r[3] + r[4]}

#  5.将解析结果写到文件中去
def write_to_file(content):
    # 写入到一个文件
    with open('result.txt','a',encoding='UTF-8') as f:
        # 通过json转为字符串的形式存储,后面是为了解决编码问题.
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

# 2.声明main方法,此时我们得到的反馈是猫眼封禁了我的IP.不要灰心,我们会解决的.
def main(offset):
    url = "http://maoyan.com/films/offset=" +str(offset) # 构造分页内容
    html = get_one_page(url)
    # print(html)
    parse_onde_page(html)


# 3.调用main方法
if __name__ == '__main__':
    for i in range(0,10):
        main(i*9) # 0-99页的数据内容.
