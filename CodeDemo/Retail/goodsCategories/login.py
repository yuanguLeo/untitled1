#!/usr/bin/env python
#_*_coding:utf-8_*_

#!/usr/bin/env python
#_*_coding:utf-8_*_

import requests
import json

class Login(object):

    def __init__(self,groupCode,userLoginName,password):

        self.groupCode = groupCode
        self.userLoginName = userLoginName
        self.password = password
        self.cookie = None

    #登录集团版
    def loginAadmin(self):
        headers = {
            "Cookie": "groupCode=27612800",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            "Referer": "https://passport.yinghezhong.com/login"
        }
        request_param_gp = {
            "groupCode": self.groupCode
        }

        request_param = {
            "userLoginName": self.userLoginName ,
            "password": self.password,
            "groupCode": self.groupCode
        }

        s = requests.session()
        r1 = s.post("https://passport.yinghezhong.com/validGroupCode", data=request_param_gp, headers=headers)
        print("r1cookie:", r1.cookies)
        print(json.dumps(r1.text))
        r2 = s.post("https://passport.yinghezhong.com/login", data=request_param, headers=headers, cookies=r1.cookies)
        print("r2cookie:", r2.cookies)
        print(json.dumps(r2.text))
        self.cookie = r2.cookies

    #选择卖品系统
    def retail(self):
        response = requests.get("https://retail.yinghezhong.com/goodsCategories/list",cookies=self.cookie)
        print(response.status_code)
        print(response.text)
