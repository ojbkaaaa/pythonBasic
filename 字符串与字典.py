# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：字符串与字典
   Description :
   Author : zhang
   date：2019/11/26
-------------------------------------------------
   Change Activity: 2019/11/26:
-------------------------------------------------
"""
__author__ = 'zhang'
# zhangStr = 'zhang zhang'
# print(zhangStr.index('z'))  # 返回'z'这个字符在zhangStr首次出现的位置
# print(zhangStr.index('z', 4))  # 相当于zhangStr[4：]
# print(zhangStr.index('z', 4, 5))  # 相当于zhangStr[4：6]，由于在该位置范围内不存在z字符，则报错
# strs = ['a','b']
# print(zhangStr.join(strs))  # 相当于使用这个zhangStr字符串对列表的元素进行连接
# print(','.join(strs))  # 使用逗号应该会比较好理解吧
#
# print(zhangStr.split('z'))  # 与join相对，split表示分割，在例子中表示已z字符进行分割，会形成一个新的列表
# print(zhangStr.split('z', maxsplit=1))  # maxsplit表示切割几次
# zhangStr = '  zhang  '
# print(zhangStr.strip(),'1')  # 表示两边去空
# print(zhangStr.lstrip(),'1')  # 去除左边的空格
# print(zhangStr.rstrip(),'1')  # 去除右边的空格
# print(zhangStr.replace('h', 'z'))  # 将字符串中的h字符进行替换
#
# print(zhangStr.count('z'))  # 统计字符串中z出现的次数
#
# print(zhangStr.endswith('z'))  # 用于判断字符串是否以z字符结尾，如果是则返回True，反之False
# print(zhangStr.startswith('z'))  # 用于判断字符串是否以z字符开头，如果是则返回True，反之False
# print(zhangStr.title())  # 返回'标题化'的字符串,就是说所有单词都是以大写开始,其余字母均为小写
# print(zhangStr.capitalize())  # 将字符串的第一个字母变成大写,其他字母变小写
# print(zhangStr.lower())  # 将字符串中的所有字符字母变小写
# print(zhangStr.casefold())  # 与lower效果一致，不过对Unicode的时候使用casefold，而lower只对ASCII的A-Z有效
# s = 'ß'
# print(s.lower())
# print(s.casefold())
# print(zhangStr.center(20, "="))  # 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
# print(zhangStr.encode("utf8"))  # 以 encoding 指定的编码格式编码字符串
# zhangStr = "\t zhang"
# print(zhangStr.expandtabs())  # 把字符串中的 tab 符号('\t')转为空格,tab 符号('\t')默认的空格数是 8
# print(zhangStr.find('a'))  # 查找并返回a字符在字符串中的位置
# print("{} {}".format("hello", "world"))  #不设置指定位置，按默认顺序
# print("{0} {1}".format("hello", "world"))  # 设置指定位置
# print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
# print("网站名：{name}, 地址 {url}".format(name="xx", url="www.xxoo.com"))
# '''
# 使用format和format_map方法都可以进行字符串格式化，但format是一种所有情况都能使用的格式化方法，
# format_map仅使用于字符串格式中可变数据参数来源于字典等映射关系数据时才可以使用
# '''
# student={'name':'小明','class':'20190301','score':597.5}
# s1='{st[class]}班{st[name]}总分：{st[score]}'.format(st=student)
# print(s1)
# student={'name':'小明','class':'20190301','score':597.5}
# s1='{class}班{name}总分：{score}'.format_map(student)
# print(s1)
#
# print(zhangStr.isalnum())  #检测字符串是否由字母和数字组成
# print(zhangStr.isalpha())  # 检测字符串是否只由字母组成
# print(zhangStr.isdecimal())  # 检查字符串是否只包含十进制字符。这种方法只存在于unicode对象
# print(zhangStr.isdigit())  # 检测字符串是否只由数字组成
# print(zhangStr.isidentifier())  # 用于判断字符串是否是有效的 Python 标识符,可用来判断变量名是否合法
# str = 'test'
# print( str.isidentifier() )  # 由于str是python的标识符，输出True
# print(zhangStr.islower())  # 检测字符串字母是否小写组成
# print(zhangStr.isnumeric())  # 检测字符串是否只由数字组成。这种方法是只针对unicode对象
#


info = {
    'name': "zhang",
    'id': "3",
    'age': "20",
}

info['home'] ='none'
print(info)
#
# print(info.pop("home")) #标准删除姿势
# print(info)
# {'stu1102': 'LongZe Luola', 'stu1103': 'XiaoZe Maliya'}
# del info['age'] #换个姿势删除
# print(info)
# info.popitem()
# print(info)
# info['age'] = 18
# print(info)

# print("age" in info) #标准用法
# print(info.get("id"))  #获取
# print(info["id"]) #同上，但是看下面
#
# print(info["car"])  #如果一个key不存在，就报错，get不会，不存在只返回None
# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
#
# av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
# print(av_catalog["大陆"]["1024"])

##### 练习
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                'xxx':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{
            '飞机场':{
                '某小店':{}
            }},
    }
}


exit_flag = False
current_layer = menu

layers = [menu]

while not  exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "q":  # 退出
        break
    elif choice == "b":  # 返回上一级
        if layers:
            current_layer = layers.pop()
        else:
            continue
    elif choice not  in current_layer:continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]









