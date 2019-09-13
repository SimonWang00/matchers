#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@Os：Windows 10 x64
@Software: PY PyCharm
@File: __NlpParser.py
@Time: 2019/8/22 18:27
@Desc: NLP to do character parsing, follow-up will be updated more
'''
import jieba.posseg as pseg

def match_name(content):
    '''
    Name Recognition

    :param content:
    :return:nameArr
    '''
    nameArr = []
    words = pseg.cut(content)
    for word, flag in words:
        if 'nr' in flag and len(word) >1:
            nameArr.append(word)
    return nameArr