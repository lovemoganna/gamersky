import requests
# 保证获得的HTML编码正确
url='http://music.baidu.com'
r = requests.get(url)
html=r.content
html_doc=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")
print(html_doc)

