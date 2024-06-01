#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Name    : setup.py
# @Author  : yanlee

import setuptools
import shutil

# 删除dist/目录
shutil.rmtree('dist', ignore_errors=True)

setuptools.setup(
    name="c-binance-future-quant",
    version="1.1.5",
    author="yanjlee",
    author_email="yanjlee@163.com",
    description="这是一套经过长时间实盘验证，有超过100亿美金交易量，包含币安合约的数据录入，风控，交易的架构实现，但不包含具体的策略，仅提供一个简单的交易实践演示数据读取，开仓，平仓，以及止盈止损，风控，还有前端数据展示和分析（前端板块为react+redux+antd，开源还在准备中，因为现在还有维护一个左侧策略，打算直接把这个左侧策略的数据释放出来示范，应该在7月25号前发布上来）你可以利用它简单，低成本的实现你的交易逻辑，其大量运用阿里云服务器进行分布式架构，多进程处理，以及飞书进行异常报错和交易信息披露...如果你愿意详细阅读该readme的所有信息，尤其是 [模块详细解析](#模块详细解析) ，那么他同时也会是一部关于币安合约的交易风控，设计架构的经验理解历史，总结了几乎本人所有成功和失败的经验，希望能让后人少踩些坑" ,
    install_requires=[
        'requests',
        'faker',
        'execjs',
        'loguru',
        'base64',
        'hashlib',
        'Crypto',
        'pandas',
        'fuzzywuzzy',
        'httpx',
        'Pillow',
        'playwright',
        'PyExecJS',
        'redis',
        'fastapi',
        'uvicorn',
        'APScheduler',
        'beautifulsoup4',
        'bs4',
        'certifi',
        'clickhouse-driver',
        'curl-cffi',
        'DrissionPage',
        'fake-useragent',
        'Flask',
        'Flask-APScheduler',
        'Flask-Cors',
        'frida',
        'gevent',
        'httpx',
        'Jinja2',
        'langchain',
        'langchain-community',
        'suiutils-py',
    ],
    long_description=open(r'readme.md', encoding='utf-8').read(),  # 读取readme自述文件
    long_description_content_type="text/markdown",
    url="https://github.com/yanjlee/c-binance-future-quant",  # 模块github地址
    packages=setuptools.find_packages(),     # 自动列出项目下的包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",   # 开源许可证
        "Operating System :: OS Independent",      # 这里的定义是系统无关（全平台兼容），如果你的包只能在部分特定系统上运行，需要修改。
    ],
)