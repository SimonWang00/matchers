#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@License: (C) Copyright 2013-2019, Best Wonder Corporation Limited.
@Os：Windows 10 x64
@Contact: bw_wangxiaomeng@whty.com.cn
@Software: PY PyCharm 
@File: __init__.py
@Time: 2019/9/13 14:43
@Desc: define your function
'''

__all__ = ["Matchers",]


import logging
from matchers.__NlpParser import match_name
from matchers.__Detector import Detectors
from matchers.__Html2Json import PageParser
from matchers.__RegularParser import commonParse,ReverseParser,ContentParser


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Matchers(object):
    def __init__(self):
        # logging.info("Let's start matchers")
        pass

    def match_content(self,html):
        '''
        General Text Analysis of Web Pages

        :param html:News Article..
        :return:content
        '''
        content = ContentParser().extract(html)
        return content

    def match_hrefs(self,doc):
        '''
        Automatic matching of all hyperlinks in a string

        :param doc:
        :return:
        '''
        hrefs = commonParse().match_href(doc)
        return hrefs

    def match_title(self,html):
        '''
        Automatic matching of page titles

        :param html:
        :return:
        '''
        titles = commonParse().match_title(html)
        return titles

    def match_email(self,content):
        '''
        Automatic matching of page emails

        :param content:
        :return:
        '''
        emails = commonParse().match_email(content)
        return emails

    def match_bankId(self,content):
        '''
        Automatic matching of page bankIds

        :param content:
        :return:
        '''
        bankIds = commonParse().match_bankId(content)
        return bankIds

    def match_IMEI(self,content):
        '''
        Automatic matching of page IMEIs

        :param content:
        :return:
        '''
        IMEIs = commonParse().match_IMEI(content)
        return IMEIs

    def match_carId(self,content):
        '''
        Automatic matching of page carIds

        :param content:
        :return:
        '''
        carIds = commonParse().match_carId(content)
        return carIds

    def match_address(self,content):
        '''
        Automatic matching of page address

        :param content:
        :return:
        '''
        address = commonParse().match_address(content)
        return address

    def match_phone(self,content):
        '''
        Automatic matching of page phones

        :param content:
        :return:
        '''
        phones = commonParse().match_phone(content)
        return phones

    def match_TaxId(self,content):
        '''
        Automatic matching of page TaxIds

        :param content:
        :return:
        '''
        TaxIds = commonParse().match_TaxId(content)
        return TaxIds

    def match_ID(self,content):
        '''
        Automatic matching of page phones

        :param content:
        :return:
        '''
        IDs = commonParse().match_ID(content)
        return IDs

    def match_Chinese(self,content):
        '''
        Automatic matching of page Chinese

        :param content:
        :return:
        '''
        Chinese = commonParse().match_Chinese(content)
        return Chinese

    def match_IP(self,content):
        '''
        Automatic matching of page IPs

        :param content:
        :return:
        '''
        IPs = commonParse().match_IP(content)
        return IPs

    def match_name(self,content):
        '''
        Automatic matching of page names

        :param content:
        :return:
        '''
        names = match_name(content)
        return names

    def _check_type(self,inputStr):
        '''
        Check InputStr Type

        :param inputStr:
        :return:html , json , text
        '''
        if '</' in inputStr and '>' in inputStr and 'class=' in inputStr:
            return "HTML"
        if "{" in str(inputStr) and "}" in str(str) == dict:
            return "JSON"
        return "TEXT"

    def _reacter(self,stat,doc):
        result = []
        if stat.get("isHref"):
            result += self.match_hrefs(doc)
        if stat.get("isTitle"):
            result += self.match_title(doc)
        if stat.get("isEmail"):
            result += self.match_email(doc)
        if stat.get("isName"):
            result += self.match_name(doc)
        if stat.get("isCarId"):
            result += self.match_carId(doc)
        if stat.get("isIMEI"):
            result + self.match_IMEI(doc)
        if stat.get("isBankId"):
            result += self.match_bankId(doc)
        if stat.get("isPhone"):
            result += self.match_phone(doc)
        if stat.get("isID"):
            result += self.match_ID(doc)
        if stat.get("isTaxId"):
            result += self.match_TaxId(doc)
        if stat.get("isIP"):
            result += self.match_IP(doc)
        return result

    def match_data_by_content(self,inputStr,doc):
        dect = Detectors()
        inputType = self._check_type(doc)
        if inputType == "HTML":
            djson = PageParser(doc).parse()
            data = ContentParser().extract_html2json_by_data(inputStr,djson)
        elif inputType == "JSON":
            data = ContentParser().extract_json_by_data(inputStr,doc)
        else:
            # TEXT type
            stat = dect(inputStr)
            data = self._reacter(stat,doc)
        return data

    def generate_regular(self,inputStr,content):
        '''
        Reverse generation of regular expressions based on matched content

        :param inputStr:
        :param content:
        :return:
        '''
        rp = ReverseParser()
        res = rp(inputStr,content)
        return res