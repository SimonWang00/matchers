Matchers
========

.. image:: https://img.shields.io/pypi/v/matchers.svg?colorB=blue
   :target: https://pypi.python.org/pypi/matchers
   :alt: PyPI Version


Overview
========

打造最好用的万能解析神器/Create the Best Universal Resolution Artifact.


Requirements
============

* Python 3.+
* Works on Linux, Windows, Mac OSX, BSD

Install
=======

The quick way::

    pip install matchers

For more details see the install section in the documentation:
https://docs.scrapy.org/en/latest/intro/install.html

Releases
========

You can find release notes at https://github.com/SimonWang00/matchers.git

Community (blog, CSDN, mail list, IRC)
=========================================

See https://blog.csdn.net/weixin_39128119

Contributing
============

See https://github.com/SimonWang00/matchers.git


Usage
-----

Usage is simple:

.. code-block:: python

    from matchers import Matchers

    content = '''
    华为创立于1987年，是全球领先的ICT（信息与通信）基础设施和智能终端提供商，我们致力于把数字世界带入每个人、每个家庭、每个组织，构建万物互联的智能世界。目前华为有18.8万员工，业务遍及170多个国家和地区，服务30多亿人口。
    地址： 深圳市龙岗区坂田华为总部办公楼。邮箱：liulinjun@huawei.com。电话：18813754316。
    官网地址http://www.huawei.com/cn/，统一社会信用代码914403001922038216。
    '''

For: Web pages, strings, and JSON. Common Analytical Examples:

.. code-block:: python

    # email提取
    >>> Matchers().match_email(content)
    2019-09-13 22:43:42,337 - root - INFO - Start commonParse engine
    ['liulinjun@huawei.com']

    # 地址提取
    >>> Matchers().match_address("服务30多亿人口。地址：深圳市龙岗区坂田华为总部办公楼。邮箱：liulinjun@huawei.com。")
    ['深圳市龙岗区坂田华为总部办公楼']

    # 手机号码提取
     >>> Matchers().match_phone(content)
    ['18813754316']

    # 通用网页正文提取
    >>> Matchers().match_content(requests.get("http://baijiahao.baidu.com/s?id=1644453217226236035&wfr=spider&for=pc").text)
    '放假通知！原来，中秋和国庆之间还有一个节！放假通知！原来，中秋和国庆之间还有一个节！大河客户端发布时间：09-1215:20大河传媒有限公司虽然刚刚开学没几天可是还是想说：中秋节、国庆节马上就到啦！高速公路小客车是否免收通行费？快一起来了解！
    ......'

Supporting Reverse Generation of Regular Expressions:

.. code-block:: python

    >>> inputStr = ["http://www.huawei.com/cn/"]
    >>> Matchers().generate_regular(inputStr,content)
    '([a-z]{4}\\:/{2}[a-z]{3}\\.[a-z]{6}\\.[a-z]{3}/[a-z]{2}/)'

According to the complete label content input, it is extended to parse all the same attributes in the whole web page.:

.. code-block:: python

    >>> url = "https://xin.baidu.com/s?q=%E7%99%BE%E5%BA%A6"
    # 想要解析所有的企业法人，只需要输入一个法人即可。
    >>> inputStr = '向海龙'
    >>> doc = requests.get(url).content.decode()
    >>> Matchers().match_data_by_content(inputStr,doc)
    ['百度', '梁志祥', '向海龙', '向海龙', '向海龙', '向海龙', '崔珊珊', '向海龙', '吴迪', '刘维', '李彦宏']


