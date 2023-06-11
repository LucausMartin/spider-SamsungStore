# 请求该地址 https://shop.samsung.com.cn/api/product/index/menu 获取 json
# 该 json 中包含了所有的商品分类信息

import requests
import json
import connectDatabase

# 定义类可进行储存
class Kind(object):
    def __init__(self, catgId, catgNm, catgCd):
        self.catgId = catgId
        self.catgNm = catgNm
        self.catgCd = catgCd
        
# 实例化数据库类
mysql = connectDatabase.Mysql()

url = 'https://shop.samsung.com.cn/api/product/index/menu'
headers = {
    'Host': 'shop.samsung.com.cn',
    'Referer': 'https://shop.samsung.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
response = requests.get(url, headers=headers)

# 转换为 json 格式获取部分数据
json_data = json.loads(response.text)
# 获取 json_data['data'] 的长度
length = len(json_data['data'])
# 遍历 json_data['data'] 获取所有的分类信息
for i in range(length):
    kind = Kind(json_data['data'][i]['catgId'], json_data['data'][i]['catgNm'], json_data['data'][i]['catgCd'])
    # 插入数据
    sql = 'insert into kind(id, name, url) values(%s, %s, %s)'
    params = (kind.catgId, kind.catgNm,"https://shop.samsung.com.cn/list/" + kind.catgCd)
    mysql.cud(sql, params)
    
# 查询数据
sql = 'select * from kind'
params = None
result = mysql.find(sql, params)
for i in result:
    print(i)