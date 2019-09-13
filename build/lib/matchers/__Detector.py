#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@Os：Windows 10 x64
@Software: PY PyCharm
@File: __Detector.py
@Time: 2019/8/22 19:16
@Desc: Detecting the types that need to be matched
'''
from  matchers.__RegularParser import commonParse
from matchers.__NlpParser import match_name


class Detectors(object):

    def __init__(self):
        self.inputStr=None

    def detector_href(self,inputStr):
        result = commonParse().match_href(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_title(self,inputStr):
        result = commonParse().match_title(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_email(self,inputStr):
        result = commonParse().match_email(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_name(self,inputStr):
        result = match_name(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_carId(self,inputStr):
        result = commonParse().match_carId(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_bankId(self,inputStr):
        result = commonParse().match_bankId(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_IMEI(self,inputStr):
        result = commonParse().match_IMEI(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_phone(self,inputStr):
        result = commonParse().match_phone(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_ID(self,inputStr):
        result = commonParse().match_ID(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_TaxId(self,inputStr):
        result = commonParse().match_TaxId(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def detector_IP(self,inputStr):
        result = commonParse().match_IP(inputStr)
        if len(result) > 0:
            return True
        else:
            return False

    def __call__(self, inputStr):
        check_stat = {}
        if self.detector_href(inputStr):
            check_stat['isHref'] = True
        if self.detector_title(inputStr):
            check_stat['isTitle'] = True
        if self.detector_email(inputStr):
            check_stat['isEmail'] = True
        if self.detector_name(inputStr):
            check_stat['isName'] = True
        if self.detector_carId(inputStr):
            check_stat['isCarId'] = True
        if self.detector_IMEI(inputStr):
            check_stat['isIMEI'] = True
        if self.detector_bankId(inputStr):
            check_stat['isBankId'] = True
        if self.detector_phone(inputStr):
            check_stat['isPhone'] = True
        if self.detector_ID(inputStr):
            check_stat['isID'] = True
        if self.detector_TaxId(inputStr):
            check_stat['isTaxId'] = True
        if self.detector_IP(inputStr):
            check_stat['isIP'] = True
        return check_stat

# dect = Detectors()
# stat = dect('王小猛的身份证号码420923199206130615，手机号码是15071348708银行卡号为6228480402564890018起后359836049182979纳税人识别92421303MA4DL45C1U，MA4DL45C-1')
# print(stat)