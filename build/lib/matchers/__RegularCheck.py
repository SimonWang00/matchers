#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@Os：Windows 10 x64
@Software: PY PyCharm
@File: __RegularCheck.py
@Time: 2019/8/23 11:20
'''

import re

class SccChecker(object):
    '''
    Unified Social Credit Code and Registration Code Verification
    '''
    @staticmethod
    def check_social_credit_code(code):
        '''
           校验统一社会信用代码的校验码
           计算校验码公式:
            C9 = 31-mod(sum(Ci*Wi)，31)，其中Ci为组织机构代码的第i位字符,Wi为第i位置的加权因子,C9为校验码
        '''
        # 第i位置上的加权因子
        # print('the code waiting for check is {}'.format(code))
        weighting_factor = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
        social_credit_check_code_dict = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'J': 18, 'K': 19, 'L': 20, 'M': 21,
            'N': 22,
            'P': 23, 'Q': 24,
            'R': 25, 'T': 26, 'U': 27, 'W': 28, 'X': 29, 'Y': 30}
        if not re.match('^[0-9a-zA-Z]+$',code):
            return False
        if code and len(code) == 18 and not re.search('(I|O|Z|S|V)',code):
            # 本体代码
            ontology_code = code[0:17]
            # 校验码
            check_code = code[17]
            # 计算校验码
            modulus = 31
            total = 0
            tmp_check_code = ""
            for i in range(len(ontology_code)):
                if ontology_code[i].isdigit():
                    total += int(ontology_code[i]) * weighting_factor[i]
                else:
                    total += social_credit_check_code_dict[ontology_code[i]] * weighting_factor[i]
                    # 当MOD函数值为0时，校验码用0表示
            if modulus - total % modulus == 31:
                tmp_check_code = list(social_credit_check_code_dict.keys())[list(social_credit_check_code_dict.values()).index(0)]
            else:
                diff = modulus - total % modulus
                tmp_check_code = list(social_credit_check_code_dict.keys())[list(social_credit_check_code_dict.values()).index(diff)]

            if tmp_check_code == check_code:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def check_register_code(code):
        '''
           校验注册码的校验码
           中国企业工商注册码前六位为行政区代码，中间8位顺序编码，最后一位为根据ISO 7064:1983.MOD 11-2校验码计算出来的检验码
        '''
        if code and len(code) == 15:
            num = code[:14]
            check_num = int(code[14])
            tmp_check_code = ""
            n = 10
            for i in range(len(num)):
                n = (int(num[i]) + n) % 10
                if n == 0:
                    n = 10
                n = n * 2 % 11
            if n == 0:
                tmp_check_code = 1
            elif n == 1:
                tmp_check_code = 0
            else:
                tmp_check_code = 11 - n

            if check_num == int(tmp_check_code):
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def check_idcode(idcard):
        '''
        校验身份证号
        :param self:
        :param code:
        :return:
        '''
        Errors = ['验证通过!', '身份证号码位数不对!', '身份证号码出生日期超出范围或含有非法字符!', '身份证号码校验错误!', '身份证地区非法!']
        area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江",
                "31": "上海", "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南",
                "42": "湖北", "43": "湖南", "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州",
                "53": "云南", "54": "西藏", "61": "陕西", "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆", "71": "台湾",
                "81": "香港", "82": "澳门", "91": "国外"}
        idcard = str(idcard)
        idcard = idcard.strip()
        idcard_list = list(idcard)
        if not re.match('(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)',idcard):
            return False
        # 地区校验
        province = (idcard)[0:2]
        if province not in area:
            return False
        # 15位身份号码检测
        if (len(idcard) == 15):
            if ((int(idcard[6:8]) + 1900) % 4 == 0 or (
                    (int(idcard[6:8]) + 1900) % 100 == 0 and (int(idcard[6:8]) + 1900) % 4 == 0)):
                ereg = re.compile(
                    '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
            else:
                ereg = re.compile(
                    '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
            if (re.match(ereg, idcard)):
                return True
            else:
                return False
        # 18位身份号码检测
        elif (len(idcard) == 18):
            # 出生日期的合法性检查
            # 闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
            # 平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
            if (int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10]) % 4 == 0)):
                ereg = re.compile(
                    '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
            else:
                ereg = re.compile(
                    '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
            # //测试出生日期的合法性
            if (re.match(ereg, idcard)):
                # //计算校验位
                S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + (int(idcard_list[1]) + int(
                    idcard_list[11])) * 9 + (int(idcard_list[2]) + int(idcard_list[12])) * 10 + (int(
                    idcard_list[3]) + int(idcard_list[13])) * 5 + (int(idcard_list[4]) + int(idcard_list[14])) * 8 + (
                            int(
                                idcard_list[
                                    5]) + int(
                        idcard_list[
                            15])) * 4 + (
                            int(
                                idcard_list[
                                    6]) + int(
                        idcard_list[
                            16])) * 2 + int(
                    idcard_list[7]) * 1 + int(idcard_list[8]) * 6 + int(idcard_list[9]) * 3
                Y = S % 11
                M = "F"
                JYM = "10X98765432"
                M = JYM[Y]  # 判断校验位
                if (M == idcard_list[17]):  # 检测ID的校验位
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False