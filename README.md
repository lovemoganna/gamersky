# gamersky
'python单线程爬取游民星空的单机游戏

目标网站:游民星空.

这里面只有`youxia.py`是正确的代码,基本步骤如下:
 
 1.制定URL的规则.利用requests模块看能不能得到相关的HTML.
 
 2.利用正则表达式解析单个页面.测试看能不能获取数据.
 
 3.创建主函数.运行上面定义的两个函数,看是否能正常运行
 
 4.之后就研究URL的规律,这个网站的URL没有进行hash加密,所以可以准确的分析出来相关的规律.
 
 5.调用主函数,循环获取数据.
 
 # 本意.
 原来是想搞猫眼电影的,结果他说我的IP被封禁了,这也是一个挑战吧.
 
 另外,我的机器很垃圾,竟然没看出多线程有多牛逼.
 
 这一点java中的多线程,有很大发挥空间.不用担心学不会.
 
 2个总结:list,dict的总结.
 
 2个挑战:设置代理,解决IP封禁.  查看多线程相关的知识.
 
 
