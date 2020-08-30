import json
import tablib

# json.text文件的格式： [{"a":1},{"a":2},{"a":3},{"a":4},{"a":5}]

# 获取ｊｓｏｎ数据
with open('json.txt', 'r', encoding='utf-8') as f:
    rows = json.load(f)
    rows = rows['assetcontent']['content']['videos']['file']
    # print(rows)
    # 将json中的key作为header, 也可以自定义header（列名）
    header = tuple([i for i in rows.keys()])
    print('header', header)
    print('rows', rows.values())
    data = []
    # 循环里面的字典，将value作为数据写入进去
    body = []
    for v in rows.values():
        body.append(v)
    data.append(tuple(body))
    print('data',data)
    data = tablib.Dataset(*data, headers=header)
    print('data', data)

    open('mdata.xlsx', 'wb').write(data.xlsx)
