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
        req = urllib.request.Request(configuration.loginurl, data, header)
        with urllib.request.urlopen(req) as resp:
            self.cookie = resp.getheader('Set-Cookie')

    def grab(self, url):
        header = {'Cookie':self.cookie}
        req = urllib.request.Request(url, headers=header)
        with urllib.request.urlopen(req) as resp:
            return resp.readall().decode('utf-8')
