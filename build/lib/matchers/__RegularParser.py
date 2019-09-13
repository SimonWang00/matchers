#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@Os：Windows 10 x64
@Software: PY PyCharm
@File: __RegularParser.py
@Time: 2019/8/22 15:47
@Desc: regular expression matching

'''

import re
import logging
from stdnum import luhn,imei
from matchers.__CreateRe import create_re
from matchers.__RegularCheck import SccChecker

class commonParse(object):
    '''
    Functions:
    Common matching methods

    '''
    def __init__(self):
        logging.info("Start commonParse engine")
        pass

    def match_href(self,content):
        '''
        url matching ,only support http,https

        :param content:
        :return:
        '''
        r = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = r.findall(content)
        return urls

    def match_title(self,content):
        '''
        web title matching

        :param content:
        :return:
        '''
        title = re.findall("<title>(.*?)</title>",content)
        return title

    def match_email(self,content):
        '''
        email matching

        :param content:
        :return:
        '''
        emails = re.findall(r"([a-z_0-9.-]{2,64}@[a-z0-9-]{2,200}\.[a-z]{2,6})", content)
        return emails

    def match_bankId(self,content):
        '''
        Bank Card Number Matching

        :param content:
        :return:
        '''
        bankIdsArr = []
        bankIds = re.findall(r"\d{19}|\d{15}",content)
        for bankId in bankIds:
            stat = luhn.is_valid(bankId)
            if stat == True:
                bankIdsArr.append(bankId)
        return bankIdsArr

    def match_IMEI(self,content):
        '''
        IMEI Number Matching

        :param content:
        :return:
        '''
        imeisArr = []
        imeis = re.findall(r"\d{17}|\d{15}",content)
        for ime in imeis:
            stat = imei.is_valid(ime)
            if stat == True:
                imeisArr.append(ime)
        return imeisArr

    def match_carId(self,content):
        '''
        License plate number matching

        :param content:
        :return:
        '''
        carIds = re.findall(r"([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1})",content)
        return carIds

    def match_address(self,content):
        '''
        Address Matching

        :param content:
        :return:
        '''
        address = re.findall(r"([\u4e00-\u9fa5\·]{6,20})",content)
        return address

    def match_phone(self,content):
        '''
        Phone Matching

        :param content:
        :return:
        '''
        phones = re.findall(r"((?:13[0-9]|14[579]|15[0-3,5-9]|17[0135678]|18[0-9])\d{8})",content)
        return phones

    def match_TaxId(self,content):
        '''
        Phone Matching

        :param content:
        :return:
        '''
        TaxIdsArr = []
        TaxIds = re.findall(r"([0-9a-zA-Z]{18})",content)
        for ids in TaxIds:
            if SccChecker().check_social_credit_code(ids):
                TaxIdsArr.append(ids)
        return TaxIdsArr

    def match_ID(self,content):
        '''
        Identity Card Number Matching :15&18

        :param content:
        :return:
        '''
        idArr = []
        IDs = re.findall(r"([1-9]\d{5}(?:1[9,8]\d{2}|20[0,1]\d)(?:0[1-9]|1[0-2])(?:0[1-9]|1[0-9]|2[0-9]|3[0,1])\d{3}[\dxX])",content) \
              + re.findall(r"([1-9]\d{7}(?:0[1-9]|1[0-2])(?:0[1-9]|1[0-9]|2[0-9]|3[0,1])\d{2}[\dxX])",content)
        for i in IDs:
            if SccChecker().check_idcode(i):
                idArr.append(i)
        return idArr

    def match_Chinese(self,content):
        '''
        Chinese Matching

        :param content:
        :return:
        '''
        chinese = re.findall(r"[\u4e00-\u9fa5]+",content)
        return chinese

    def match_IP(self,content):
        '''
        IP address Matching

        :param content:
        :return:
        '''
        ips = re.findall("((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))",content)
        return ips

class ContentParser(object):
    '''
    Function:

    General Text Extraction ,Parse Data By Content

    '''
    def __init__(self):
        logging.info("Start ContentParser engine")
        self.start = 0
        self.end = 0

    def extract_json_by_data(self,inputStr,content):
        '''
        Matching JSON lists based on content
        :param inputStr:json's content
        :param content:json list
        :return:
        '''
        try:
            content = eval(str(content))
            jsoniter = self.dict_generator(content)
            datas = list(jsoniter)
            for i in datas:
                if inputStr == i[-1]:
                    flag = '.'.join(i[0:-1])
                    data = [i[-1] for i in datas if '.'.join(i[0:-1])==flag]
                    return data
        except Exception as e:
            print("input content type only suport json. err:",e)

    def extract_html2json_by_data(self,inputStr,content,fillter=None):
        '''
        Matching HTML2JSON lists based on content
        :param inputStr:json's content
        :param content:json list
        :return:
        eg:
        {'name': 'title', 'content': 'xxx', 'attributes': {'class': ['legal-txt'],'title': 'xx'}}
        '''
        try:
            flag_list = []
            content = eval(str(content))
            jsoniter = self.dict_generator(content)
            datas = list(jsoniter)[0]
            for i in datas:
                if inputStr == i["content"]:
                    if i["attributes"]:
                        attr = (i["name"],i["attributes"].keys())
                        if attr not in flag_list:
                            flag_list.append((attr))
            if len(flag_list) == 1:
                result = [data["content"] for data in datas if data["attributes"] and \
                          data["attributes"].keys()==flag_list[0][1] and data['name']==flag_list[0][0]]
            else:
                logging.warning("Be careful! The input content has multiple tag matches in the web page")
                result = []
                for data in datas:
                    if data["attributes"] and (data['name'],data["attributes"]) in flag_list:
                        result.append(data["content"])
            if fillter:
                result = [r for r in result if fillter==r]
            return result
        except Exception as e:
            print("input content type only suport json. err:",e)

    def dict_generator(self,indict, pre=None):
        '''
        Recursive parsing JSON
        :param indict:
        :param pre:
        :return:
        '''
        pre = pre[:] if pre else []
        if isinstance(indict, dict):
            for key, value in indict.items():
                if isinstance(value, dict):
                    if len(value) == 0:
                        yield pre+[key, '{}']
                    else:
                        for d in self.dict_generator(value, pre + [key]):
                            yield d
                elif isinstance(value, list):
                    if len(value) == 0:
                        yield pre+[key, '[]']
                    else:
                        for v in value:
                            for d in self.dict_generator(v, pre + [key]):
                                yield d
                elif isinstance(value, tuple):
                    if len(value) == 0:
                        yield pre+[key, '()']
                    else:
                        for v in value:
                            for d in self.dict_generator(v, pre + [key]):
                                yield d
                else:
                    yield pre + [key, value]
        else:
            yield indict

    def remove_js_css (self,content):
        '''
        Notes:
        Remove deletes head, jss, annotations and CSS files from the web
        :param content:web
        :return:
        '''
        r = re.compile(r'''<script.*?</script>''',re.I|re.M|re.S)
        s = r.sub ('',content)
        # r = re.compile(r'''<head.*?</head>''', re.I|re.M|re.S)
        # s = r.sub('',s)
        r = re.compile(r'''<style.*?</style>''',re.I|re.M|re.S)
        s = r.sub ('', s)
        r = re.compile(r'''<!--.*?-->''', re.I|re.M|re.S)
        s = r.sub('',s)
        r = re.compile(r'''<meta.*?>''', re.I|re.M|re.S)
        s = r.sub('',s)
        r = re.compile(r'''<a.*?</a>''', re.I|re.M|re.S)
        s = r.sub('',s)
        r = re.compile(r'''<ins.*?</ins>''', re.I|re.M|re.S)
        s = r.sub('',s)
        return s

    def remove_empty_line (self,content):
        '''
        Notes:
        Delete blank lines
        :param content:web
        :return:
        '''
        r = re.compile(r'''^\s+$''', re.M|re.S)
        s = r.sub ('', content)
        r = re.compile(r'''\n+''',re.M|re.S)
        s = r.sub('\n',s)
        return s

    def remove_any_tag (self,content):
        '''
        Notes:
        Remove Html tags
        :param content:web
        :return:
        '''
        s = re.sub(r'''<[^>]+>''','',content)
        return s.strip()

    def remove_any_tag_but_a (self,content):
        '''
        Delete the Html tag but keep the a tag
        :param content:web
        :return:
        '''
        text = re.findall (r'''<a[^r][^>]*>(.*?)</a>''',content,re.I|re.S|re.S)
        text_b = self.remove_any_tag (content)
        return len(''.join(text)),len(text_b)

    def remove_image (self,content,n=50):
        '''
        Delete the image and give it a weight of 50

        :param content:web
        :param n:weight
        :return:
        '''
        image = 'a' * n
        r = re.compile (r'''<img.*?>''',re.I|re.M|re.S)
        s = r.sub(image,content)
        return s

    def remove_video (self,content,n=1000):
        '''
        Remove the video and grant 1000 privileges

        :param content:web
        :param n:weight
        :return:
        '''
        video = 'a' * n
        r = re.compile (r'''<embed.*?>''',re.I|re.M|re.S)
        s = r.sub(video,content)
        return s

    def sum_max (self,values):
        '''
        Find the sudden drop point according to the number of blocks

        Left is the rising point of the text and right is the ending point of the text.

        Values: A list of blocks in HTML
        :param values:the number of blocks
        :return:
        '''
        cur_max = values[0]
        glob_max = -999999
        # Find the end of the text
        for index,value in enumerate (values):
            cur_max += value
            if cur_max > glob_max :
                glob_max = cur_max
                self.end = index
            elif cur_max < 0:
                cur_max = 0
        # glob_max It's the cumulative point of content. Back off point by point to find the starting point of the text.
        for i in range(self.end, -1, -1):
            glob_max -= values[i]
            if abs(glob_max < 0.000001):
                self.start = i
                break
        return self.start,self.end+1

    def method_1 (self,content, k=1):
        '''
        Processing the web, default k = 1

        :param content:web
        :param k:steps
        :return:
        '''
        if not content:
            return "Web content is none"
        tmp = content.split('\n')
        group_value = []
        for i in range(0,len(tmp),k):
            group = '\n'.join(tmp[i:i+k])
            group = self.remove_image (group)
            group = self.remove_video (group)
            text_a,text_b= self.remove_any_tag_but_a (group)
            temp = (text_b - text_a) - 8
            group_value.append (temp)
        start,end = self.sum_max (group_value)
        return start,end, len('\n'.join(tmp[:start])), len ('\n'.join(tmp[:end]))

    def extract (self,content):
        '''
        Main Method of Extracting Text

        :param content:web
        :return:text
        '''
        try:
            content = self.remove_empty_line(self.remove_js_css(content))
            start,end,x,y = self.method_1 (content)
            txt = '\n'.join(content.split('\n')[start:end])
            txt = self.remove_any_tag(txt)
            return txt
        except Exception as e:
            print("Error type：",e)


class ReverseParser(object):
    '''
    Reverse generation of regular expressions based on matched content
    '''
    def __init__(self):
        logging.info("Start ReverseParser engine")
        pass

    def __call__(self, inputStr,content):
        '''
        Program Execution Entry

        :param inputStr:Target string
        :param content:Text that needs to be matched
        :return:regular expression
        '''
        cur=create_re()
        RES=cur.run(content,inputStr,tag=True)
        check_result=cur.check_res(RES,tag=True)
        if check_result:
            return RES
        else:
            logging.warning("Regular expressions may be incorrect. Check yourself !")
            return RES.split()[0]