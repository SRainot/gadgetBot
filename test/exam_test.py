# -*- coding: utf-8 -*-
# Author:w k


import requests

target_url = 'https://jx3.derzh.com/exam/?m=1&q=%E9%9D%92%E5%B2%A9&csrf='
result = requests.get(target_url, verify=False).json()
for item in result.get('result', []):
    print(item)