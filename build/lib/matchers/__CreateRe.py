#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@Os：Windows 10 x64
@Software: PY PyCharm
@File: __CreateRe.py
@Time: 2019/8/22 17:04
@Desc: Reverse Generation of Regular Expressions Based on Content
'''

#! -*- coding:utf-8 -*-

__author__="nMask,SimonKing"
__Date__="2019.08.22"
__version__="1.0"
__py_version__="2.7.11,3.6"


import re
import string


class create_re(object):

    DICT = {

        "1":"\d", #int
        "2":"[a-z]", #str_low
        "4":"[A-Z]", #str_up
        "6":"[a-z,A-Z]", #str_low_up
        "3":"[a-z,0-9]", #str_low+int
        "5":"[A-Z,0-9]", #str_up_int
        "7":"\w", # str+int
        "1000":"(?:.?)",  # any str
        "2000":"\s?", # include \r\n
    }

    RE_DICT = {

        "email":r"([a-z_0-9.-]{2,64}@[a-z0-9-]{2,200}\.[a-z]{2,6})",
        "phone":r"((?:13[0-9]|14[579]|15[0-3,5-9]|17[0135678]|18[0-9])\d{8})",
        "name":r""+u"([\u4e00-\u9fa5\·]{2,3})",
        "id_18":r"([1-9]\d{5}(?:1[9,8]\d{2}|20[0,1]\d)(?:0[1-9]|1[0-2])(?:0[1-9]|1[0-9]|2[0-9]|3[0,1])\d{3}[\dxX])",
        "id_15:":r"([1-9]\d{7}(?:0[1-9]|1[0-2])(?:0[1-9]|1[0-9]|2[0-9]|3[0,1])\d{2}[\dxX])",
        "car_id":r"([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1})",
        "address":r"([\u4e00-\u9fa5\·]{6,20})"
    }

    ZY = ["*","\'","\"","[","]",".","(",")","{","}","\\","?","+","^","$","|","@","#","!",",","_","%","&","\/",";","=",":"] #需要转义的字符

    # Special characters,. can't match.
    STR_OTHER = ["\n","\r","\n\r","\r\n"]

    def is_int(self,str_):
        '''check str is int type or not?'''

        try:
            int(str_)
            return True
        except:
            return False

    def is_str_low(self,str_):
        '''check str is string and low or not?'''

        if str_ in string.ascii_lowercase:
            return True
        else:
            return False

    def is_str_up(self,str_):
        '''check str is string and up or not?'''

        if str_ in string.ascii_uppercase:
            return True
        else:
            return False

    def list_in_list(self,list_,S):
        '''
        Judgment result list

        :param list_:
        :param S:
        :return:
        '''
        for i in S:
            if i not in list_:
                return False

        return True


    def check_res(self,res,tag=False):
        '''
        Check Re

        :param res:
        :param tag:
        :return:
        '''
        try:
            p_res = re.compile(res)
        except:
            return False
        else:
            result = p_res.findall(self.STRING)
            result_set=list(set(result))

            if result == self.S:
                return result
            elif result_set == self.S:
                return result_set
            else:
                if tag:
                    # Contains matches: as long as the desired value exists in the result list
                    if self.list_in_list(result,self.S):
                        return result
                    elif self.list_in_list(result_set,self.S):
                        return result_set
                    else:
                        pass

                return False


    def judge_type(self,str_):
        '''
        judge str type
        :param str_:
        :return:
        '''
        if self.is_int(str_):
            return (1,str_)
        elif self.is_str_low(str_):
            return (2,str_)
        elif self.is_str_up(str_):
            return (4,str_)
        else:
            return (1000,str_)

    def sa(self,list_str):
        tag=0
        list_str=list(set(list_str))

        for i in list_str:
            if i:
                tag+=1
        return tag


    def con_list(self,list_):
        '''
        calc str type

        :param list_:
        :return:
        '''

        list_n=[i[0] for i in list_]

        list_str=[i[1] for i in list_ if i[1]]

        sum_=sum(list(set(list_n)))

        if sum_>=1000:
            if self.sa(list_str)>1:
                return "1000"
            else:
                key=list_str[0]
                if key in self.ZY:
                    return "\\"+key
                else:
                    return key
        else:
            return str(sum_)


    def crate_res(self,max_num):
        '''
        Generating regular expressions
        :param max_num:
        :return:
        '''

        RES = r""
        tag_=""
        num_=1

        for n_,n in enumerate(range(max_num)):
            a=[]
            for i in self.S:
                try:
                    rs=self.judge_type(i[n])
                except:
                    #(0,"(?:.?)")
                    rs=(1000,"(?:.?)")
                a.append(rs)

            key=self.con_list(a)
            tag=self.DICT.get(key,key)

            if tag==tag_:
                #last str
                if n_==max_num-1:
                    tag_=tag
                    if num_>1:
                        RES+="{"+str(num_+1)+"}"
                        num_=1
                    else:
                        RES+=tag
                else:
                    num_+=1
            else:
                tag_=tag
                if num_>1:
                    RES+="{"+str(num_)+"}"
                    num_=1
                RES+=tag


        RES="("+RES+")"

        return RES



    def left(self,RES,tag=False):
        '''
        Front position, adjust regular expression
        :param RES:
        :param tag:
        :return:
        '''

        num=10
        for i in range(num):
            if self.check_res(RES,tag=tag):
                break
            else:
                start_list=[]
                for str_ in self.S:
                    get_str_number=self.STRING.find(str_)
                    start = self.STRING[get_str_number-(i+1)]
                    start_list.append(start)

                if len(list(set(start_list)))==1:
                    if start in self.ZY:
                        start = "\\" + start
                    if start in self.STR_OTHER:
                        break
                    RES = start+RES
                else:
                    break

        return RES


    def right(self,RES,tag=False):
        '''
        Postposition, Regular Expression Adjustment
        :param RES:
        :param tag:
        :return:
        '''
        num=10
        for i in range(num):
            if self.check_res(RES,tag=tag):
                break
            else:
                end_list=[]
                try:
                    for str_ in self.S:
                        get_str_number = self.STRING.find(str_)
                        end = self.STRING[get_str_number+len(str_)+i]
                        end_list.append(end)

                    if len(list(set(end_list)))==1:
                        if end in self.ZY:
                            end = "\\" + end
                        if end in self.STR_OTHER:
                            break

                        RES = RES+end
                    else:
                        break
                except:
                    break
        return RES


    def get_res(self,type_="email"):
        r=self.RE_DICT.get(type_,"")
        return r

    def run(self,STRING,S,tag=False):
        '''
        run start create res
        :param STRING:
        :param S:
        :param tag:
        :return:
        '''

        if isinstance(STRING, str):

            self.STRING = STRING
            self.S = S
            # Calculate the length of the field with the longest list result
            max_num=sorted([len(i) for i in self.S],reverse = True)[0]
            try:
                # Generate preliminary regular expressions
                RES_=self.crate_res(max_num)
            except UnicodeDecodeError:
                print ("[Error]Please check your input list , chinese must be unicode, Set like [u'你好'] ")
            else:
                # Generate regular expressions that add strings to the left
                RES=self.left(RES_,tag=tag)
                # Generate regular expressions that add strings to the right
                RES=self.right(RES,tag=tag)

                if self.check_res(RES,tag=tag):
                    return RES
                elif tag is False:
                    # Generate regular expressions that add strings to the left
                    RES=self.left(RES_,tag=True)
                    # Generate regular expressions that add strings to the right
                    RES=self.right(RES,tag=True)
                return RES

        else:
            print ("[Error]Please input unicode type string !")