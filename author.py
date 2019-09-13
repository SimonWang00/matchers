#!/usr/bin/python3
# __*__ coding: utf-8 __*__

'''
@Author: simonKing
@License: (C) Copyright 2013-2019, Best Wonder Corporation Limited.
@Os：Windows 10 x64
@Contact: bw_wangxiaomeng@whty.com.cn
@Software: PY PyCharm 
@File: author.py
@Time: 2019/9/13 17:03
@Desc: define your function
'''

from otpauth import OtpAuth
'''
>>> auth = OtpAuth('secret')  # a secret string
>>> auth.hotp()
330810
>>> auth.valid_hotp(330810)
4
>>> auth.hotp(2)
720111
>>> auth.valid_hotp(720111)
2
>>> auth.totp()  # a time based string
828657
>>> auth.valid_totp(828657)
True
'''

def qrCoderValid(inputStr):
    auth = OtpAuth(inputStr)
    hotp_code = auth.hotp(6)
    valid = auth.valid_hotp(hotp_code)
    # hotp_code = auth.hotp(6)
    # valid = auth.valid_hotp(hotp_code)
    totp_code = auth.totp(period=30,)
    print(totp_code)
    if auth.valid_totp(totp_code):
        return totp_code
    return totp_code


def googleScan(inputStr):
    from otpauth import OtpAuth
    auth = OtpAuth(inputStr)  # a secret string
    # to_google(self, type, label, issuer, counter=None)
    s = auth.to_google(type='totp', issuer="PyPI", label='SHA1',counter='6')
    print(s)
    return s

# inputStr = "NGO4WFHPWZNYAKDQJDFGYAPQ426CCD72"
inputStr = "NGO4WFHPWZNYAKDQJDFGYAPQ426CCD72"
if qrCoderValid(inputStr):
    print(True)
# qrCoderValid(inputStr)
# googleScan(inputStr)
