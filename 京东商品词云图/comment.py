"""
    日期：2019.07.26.
    功能：爬取京东商品信息
"""

import time
import requests


headers={
    'Referer': 'https://item.jd.com/26414687140.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def spider_comment(product, x, f):
    url = 'http://sclub.jd.com/comment/productPageComments.action?&procuctId=26414687140' \
          '&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    # 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv346
    # &productId=26414687140&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
    # 删掉callback=fetchJSON_comment98vv346，只返回json数据
    response = requests.get(url, headers=headers)
    time.sleep(3)
    content = response.json()
    infos = content["comments"]
    for info in infos:
        print(info["content"])
        print('-------------------------------------')
        f.write(info['comment'])


if __name__ == '__main__':
    spider_comment()
    productId = input('请输入你要爬取的商品Id:')
    with open('jd_comment_%s.txt'%productId, 'a+', encoding='utf-8') as f:
        # 构建页面
        for x in range(100):
            spider_comment(productId, x, f) # 43
