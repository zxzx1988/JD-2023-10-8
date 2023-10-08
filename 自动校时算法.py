import json
import time

import requests


# wskey=AAJk1yn6AEDSkuoh_R_rVs68Zd4tD9BwNJoxUjvWQUuW-vOnSiWDLrptu7Fg56ywZaPcJACtDzjec9KopCeqwC1hPSKP-uvW;whwswswws=JD0111d47dh23mtkCZT2169517901754904MYqNbuqMaPUmiPGJzdjO722GjIBOdVE38_dYjoSaJkJCeW-IWlkbSqOI_R6VgDDW84DVbVs3DPx6FYGwEgKJUjiDsIgBW6-dYABiMTFwVbM0i69dlm~AAjMMi7CKEfOmMihF9JpnseUxyDOBQbxAc-PNagAAAA53ZFVIQ1V2YUtkYW9tbQ;unionwsws={"jmafinger":"JD0111d47dh23mtkCZT2169517901754904MYqNbuqMaPUmiPGJzdjO722GjIBOdVE38_dYjoSaJkJCeW-IWlkbSqOI_R6VgDDW84DVbVs3DPx6FYGwEgKJUjiDsIgBW6-dYABiMTFwVbM0i69dlm~AAjMMi7CKEfOmMihF9JpnseUxyDOBQbxAc-PNagAAAA53ZFVIQ1V2YUtkYW9tbQ","devicefinger":"eidIc11281210cs70PmWgaoKQzC+zNCtvs4P3dD5mAuShiRsxafFMGVcd10\/Y4VCZCU\/TnJEc6QPJEiD47thQMk59x2tMJP7F4iy1qs4jVhEKMSQBNx6"};pin_hash=257593892



class JDTimer:

    def __init__(self):
        self.headers = {
            'user-agent': 'okhttp/3.12.1;jdmall;android;version/10.5.0;build/95837;',
            'content-type': 'application/x-www-form-urlencoded',
        }
        self.session = requests.Session()
        try:
            self.jd_time()
        except Exception as e:
            print(e)

    # def jd_time(self):
    #     """
    #     从京东服务器获取时间毫秒
    #     :return:
    #     """
    #     url = 'https://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5'
    #     ret = self.session.get(url, headers=self.headers, allow_redirects=False, verify=False).text
    #     js = json.loads(ret)

    #     return int(js["currentTime2"])

    def jd_time(self):
        """
        从京东服务器获取时间毫秒
        :return:
        """
        response = requests.get('https://api.m.jd.com/')
        abccc=response.headers.get('X-API-Request-Id')[-13:]
        return int(abccc)

    def local_time(self):
        """
        获取本地毫秒时间
        :return:
        """
        return int(round(time.time() * 1000))

    def local_jd_time_diff(self):
        """
        计算本地与京东服务器时间差
        :return:
        """
        try:
            return self.local_time() - self.jd_time()
        except Exception as e:
            print(e)
            return 0

if __name__ == '__main__':
    jdtimer = JDTimer()
    for i in range(5):
        print(jdtimer.local_jd_time_diff())
