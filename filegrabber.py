__author__ = 'Rick Qiu'

import configuration
import urllib.request
import urllib.response
import urllib.parse

class FileGrabber:
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
            return resp.readall().decode()

if __name__ == "__main__":
    grabber = FileGrabber()
    doc = grabber.grab('http://community.topcoder.com/tc?module=ProblemArchive&sc=0&sd=asc&er=10000')
    import bs4
    soup = bs4.BeautifulSoup(doc)
    print(soup.prettify())