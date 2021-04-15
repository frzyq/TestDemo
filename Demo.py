import requests
import json
import hashlib

class translate():
    def __init__(self,query_str):
        self.query_str =query_str
        url= 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
        sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1" + self.query_str).encode('utf-8')).hexdigest())[0:16]
        self.url = url + "&sign=" + sign
        self.headers={
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }

        self.data=self.get_data()


    def get_data(self):
      data={
          "from": "auto",
          "to:":"auto",
          "q": self.query_str
      }
      return data


    def get_data_tran(self):
        response=requests.post(self.url,headers=self.headers,data=self.data)
        return response.content.decode()

    def parse_data(self,json_str):
        dict_data=json.loads(json_str)
        try:
            result = dict_data["content"]['out']
            print("translation:{}  \n Results after translation ：{}""".format(self.query_str,result))
        except:
            print("无法翻译，该语句中可能含有敏感词汇，请重新输入")


    def run(self):
        json_str=self.get_data_tran()
        self.parse_data(json_str)


if __name__=='__main__':
    query_str= input("Please enter your translation：")
    tr =translate(query_str)
    tr.run()

