#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@License: (C) Copyright 2013-2019, Best Wonder Corporation Limited.
@Os：Windows 10 x64
@Contact: bw_wangxiaomeng@whty.com.cn
@Software: PY PyCharm 
@File: test.py
@Time: 2019/8/22 17:14
@Desc: define your function
'''
import time
import requests
from matchers import Matchers

# 待匹配的字符串
content = '''
        Python从设计之初就已经是一门面向对象的语言，420923199106310648正因为如此，刘邦。429023199206130618本章节我们将详细介绍Python的面向对象编程。
        还有java 、张三丰开车车牌号鄂ACC929，然后学会了cpp等等都是支持面向对象的https://github.com/,百度一下https://www.baidu.com/.我的邮箱地址simon_wang00@163.com
        湖北省武汉市洪山区关东康居园，15572023513我在孝感市云梦县西单路锦绣花园11栋西单元102房间里面等你，我的车牌号码是鄂A16189，我的IP地址是192.168.3.2,换号码了呀13733425781
        '''

def test_create_re():
    try:
        # 预想匹配结果列表
        S = ["py"]

        # 代表开启贪婪模式
        tag=True
        check_result = Matchers().generate_regular(S,content)

        print ("check:",check_result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_create_re()




def test_match_title():
    try:
        result = Matchers().match_title(requests.get("https://www.baidu.com/").content.decode())
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_title()

def test_match_email():
    try:
        result = Matchers().match_email(content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_email()

def test_match_name():
    try:
        result =Matchers().match_name(content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_name()


def test_match_carId():
    try:
        result = Matchers().match_carId(content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_carId()

def test_match_address():
    try:
        result = Matchers().match_address("送货地址：孝感市云梦县西单路锦绣花园15栋西单元602房间张三收")
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_address()

def test_match_phone():
    try:
        result = Matchers().match_phone(content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_phone()

def test_match_ID():
    try:
        result = Matchers().match_ID(content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_ID()

def test_match_Chinese():
    try:
        result = Matchers().match_Chinese(content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_Chinese()

def test_match_IP():
    try:
        result = Matchers().match_IP(content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_IP()

def test_match_extract():
    try:
        result = Matchers().match_content(requests.get("https://www.baidu.com/").content.decode())
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_match_extract()


def test_Matchers_Functions():
    try:
        url = "https://xin.baidu.com/s?q=%E7%99%BE%E5%BA%A6"
        inputStr = '向海龙'
        doc = requests.get(url).content.decode()
        result = Matchers().match_data_by_content(inputStr,doc)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_Matchers_Functions()


def test_generate_regular():
    try:
        # inputStr = ["15572023513"]
        inputStr = ["py"]
        result = Matchers().generate_regular(inputStr,content)
        print(result)
        print("test result : PASS")
    except:
        print("test result : FAILD")

# test_generate_regular()

# from matchers.matchers import matchers
#
# matchers().match_IP(content)
# matchers().match_phone(content)