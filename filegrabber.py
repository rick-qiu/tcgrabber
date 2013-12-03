__author__ = 'Rick Qiu'

import configuration
import urllib.request
import urllib.response
import urllib.parse

class filegrabber:
    def __init__(self):
        data = urllib.parse.urlencode(query={'username':configuration.username,
                                             'password':configuration.password,
                                             'rememberMe':'true'}).encode('utf-8')
        header = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8"}
        loginurl = 'http://www.topcoder.com/present/login'
        req = urllib.request.Request(loginurl, data, header)

        proxy = urllib.request.ProxyHandler(configuration.proxies)
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)

        with urllib.request.urlopen(req) as resp:
            self.cookie = resp.getheader('Set-Cookie')

    def grab(self, url):
        header = {'Cookie':self.cookie}
        req = urllib.request.Request(url, headers=header)
        with urllib.request.urlopen(req) as resp:
            return resp.readall().decode('utf-8')

if __name__ == "__main__":
    grabber = filegrabber()
    resp = grabber.grab('http://community.topcoder.com/stat?c=problem_statement&pm=12790&rd=15708')
    print(resp)