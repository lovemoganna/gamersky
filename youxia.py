import json
import re
#引入多线程模块中的池子
from multiprocessing import Pool
import requests
from requests import RequestException

# 1.获得HTML页面
def get_one_page(url):
    try:
        response = requests.get (url)
        # 确保下载的HTML不是乱码.
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
# 3.解析这个页面
def parse_one_page(html):
    pattern = re.compile('<li.*?bgimg_xxs.*?Img_L.*?<a.*?img\ssrc="(.*?)".*?Img_R.*?'
                          +'ImgR_1.*?<a\shref="(.*?)".*?>(.*?)</a>'
                          +'.*?ImgR_2.*?ImgR2">.*?<span>(.*?)</span>(.*?)</div>'
                          +'.*?ImgR2">.*?<span>(.*?)</span>(.*?)</div>' + '.*?ImgR2">.*?<span>(.*?)</span>(.*?)</div>'
                          +'.*?ImgR_2 bgimg_xx.*?ImgR2">.*?<span>(.*?)</span>(.*?)</div>'
                          +'.*?ImgR2">.*?<span>(.*?)</span>(.*?)</div>'
                          +'.*?</li>',re.S)
    # ('http://img1.gamersky.com/image2015/08/20150828zpf_2/gamersky_01small_02_2015828941960.jpg', 'http://down.gamersky.com/tv/201508/656310.shtml', '《合金装备5：幻痛》X360英文IOS版下载', '发布时间：', '2015-08-28', '游戏大小：', '16.28 GB', '推荐等级：', '★★★', '游戏类型：', '动作游戏', '游戏语言：', '英文')
    # 我们想以dict形式输出,所以起名时间到了,[0,1,2,4,6,8,10,12]:[gameImage,gameUrl,gameTitle,releaseTime,gameSize,gameContent,GameLanguage]
    items = re.findall(pattern,html)
    # 测试是否正确输出
    # for i in items:
    #     print(i)

   # 组建dict 元组,方便输出.
    for item in items:
        yield{
            'gameImage:': item[0],
            'gameUrl:' :item[1],
            'gameTitle:':item[2],
            'releaseTime:':item[4],
            'gameSize:': item[6],
            'recommendationLevel': item[8],
            'gameContent:': item[10],
            'GameLanguage:': item[12],
        }

# 4.写入到一个文件中去
def write_to_file(content):
    # 写入到一个文件
    with open('youxiawang.txt','a',encoding='UTF-8') as f:
        # 通过json转为字符串的形式存储,后面是为了解决编码问题.
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

# 2.定义主方法
def main(num):
    if num > 0 and num <75:
        url = 'http://down.gamersky.com/oth/te/List_'+str(num)+'.shtml'
    else:
        url = 'http://down.gamersky.com/oth/te/'
    html = get_one_page (url)
    # 遍历我们组建的dict
    for item in parse_one_page(html):
        print(item)
        # 每遍历一次写入一次
        write_to_file(item)

if __name__ == '__main__':
    # 多线程去运行
    pool = Pool ()
    pool.map (main, [i -10 for i in range (74)])  # 将数组中的每一个元素拿出来当做函数的参数,创建一个个进程,放进进程池中去运行.
    # 单线程去运行
    # for i in range(0,74):
    #     main(i)




