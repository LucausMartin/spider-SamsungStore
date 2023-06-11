# 通过 https://shop.samsung.com.cn/api/product/plp/v2/page 获取商品种类 jso

import requests
import connectDatabase
import json

# 连接数据库
mysql = connectDatabase.Mysql()


# 定义商品类
class Goods(object):
    def __init__(self, prodId, prodNm, prodPrice):
        self.prodId = prodId
        self.prodNm = prodNm
        self.prodPrice = prodPrice


def get_goods(name):
    url = 'https://shop.samsung.com.cn/api/product/plp/v2/page'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'shop.samsung.com.cn',
        'Origin': 'https://shop.samsung.com.cn',
        'Referer': 'https://shop.samsung.com.cn/product/100000000000000307.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }
    if name == "smartphone-tablet":
        data = {
            "catgLvlTwoCd": "",
            "catgLvlOneCd": name,
            "orderBy": [],
            "pageSize": 999,
            "pageNo": 1,
            "prodTags": "",
            "minPrice": "",
            "maxPrice": "",
            "categoryIds": [
                1009,
                1005,
                1006,
                1008
            ],
            "tagCdList": []
        }
    elif name == "wearable":
        data = {
            "catgLvlTwoCd": "",
            "catgLvlOneCd": "wearables",
            "orderBy": [],
            "pageSize": 90,
            "pageNo": 1,
            "prodTags": "",
            "minPrice": "",
            "maxPrice": "",
            "categoryIds": [],
            "tagCdList": []
        }
    else:
        data = {
            "catgLvlTwoCd": "",
            "catgLvlOneCd": name,
            "orderBy": [],
            "pageSize": 999,
            "pageNo": 1,
            "prodTags": "",
            "minPrice": "",
            "maxPrice": "",
            "categoryIds": [],
            "tagCdList": []
        }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # 转换为 json 格式获取部分数据
    json_data = json.loads(response.text)
    # 将每一个商品的 id 存进数组
    id_list = []
    temp_list = []
    for i in range(len(json_data['data']['pageData'])):
        # 以符号 / 分割字符串
        temp_list.append(json_data['data']['pageData']
                         [i]['prodCd'].split('/')[0])
        # 判断每一个最后两个字母是不是 ZS
        if temp_list[i][-2:] != 'ZS':
            id_list.append(temp_list[i])
    print(id_list)

    # 根据 id_list 获取商品信息通过在 https://shop.samsung.com.cn/api/product/pdp/skuInfoList/ 后加上商品 id
    # 获取商品信息
    for i in range(len(id_list)):
        url = 'https://shop.samsung.com.cn/api/product/pdp/skuInfoList/' + \
            id_list[i]
        print(url)
        headers = {
            'Host': 'shop.samsung.com.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.get(url, headers=headers)
        # 转换为 json 格式获取部分数据
        json_data = json.loads(response.text)
        # 获取商品数据
        for i in range(len(json_data['data'])):
            # 商品 id
            prodId = json_data['data'][i]['skuId']
            # 商品名称
            prodNm = json_data['data'][i]['skuNm']
            # 商品价格
            prodPrice = json_data['data'][i]['price']
            # 实例化商品类
            goods = Goods(prodId, prodNm, prodPrice)
            print(goods.prodId, goods.prodNm, goods.prodPrice)
            # 将商品数据存入数据库
            # sql 语句
            if name == 'smartphone-tablet':
                name = 'phone'
            elif name == 'tv-av':
                name = "tv"
            elif name == "smart-home-appliances":
                name = "smart_home"
            elif name == "office-storage":
                name = "storage"
            sql = 'insert into ' + name + \
                '(id, name, price) values(%s, %s, %s)'
            #  sql 语句参数
            param = (goods.prodId, goods.prodNm, goods.prodPrice)
            # 执行 sql 语句
            mysql.cud(sql, param)


# 主函数
if __name__ == '__main__':
    get_goods("smartphone-tablet")
    get_goods("wearable")
    get_goods("tv-av")
    get_goods("smart-home-appliances")
    get_goods("office-storage")