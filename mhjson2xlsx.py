import json
import tablib
import xmltodict

xmlFilePath = r"E:\myDocument\mgwork\消息工单\集合.txt"
jsonFileName = 'jsonjh.txt'
xml_file = open(xmlFilePath, 'r', encoding='utf-8')
xml_str = xml_file.read()

jsonStr = json.dumps(xmltodict.parse(xml_str), indent=4)

# print(jsonStr)
f = open(jsonFileName, "w")

print(jsonStr, file=f)
f.close()

# 解析json数据
with open(jsonFileName, 'r', encoding='utf-8') as f:
    rows = json.load(f)
    rows = rows['assetcontent']['content']
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
    print('data', data)
    data = tablib.Dataset(*data, headers=header)
    print('data', data)

    open('mjhdata.xlsx', 'wb').write(data.xlsx)
