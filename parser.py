__author__ = 'Rick Qiu'

from bs4 import BeautifulSoup

def parse_problem_archive(htmldoc):
    """
    This function is to handle below page:
    http://community.topcoder.com/tc?module=ProblemArchive&sc=0&sd=asc&er=10000
    it returns a list and each element is a diction like below:
    {'name':'Aaagmnrs',
    'url':'http://community.topcoder.com/stat?c=problem_statement&pm=2854',
    'contest':'SRM204',
    'detail':'http://community.topcoder.com/tc?module=ProblemDetail&rd=5850&pm=2854'}
    """
    row_selector = "html > body > table:nth-of-type(1) > tbody > tr > td:nth-of-type(3) > table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td > form > table:nth-of-type(4) > tbody > tr:nth-of-type(3)"
    name_selector = "td:nth-of-type(2) > a"
    contest_selector = "td:nth-of-type(3) > a"
    date_selector = "td:nth-of-type(4)"
    categories_selector = "td:nth-of-type(6)"
    div1level_elector = "td:nth-of-type(7)"
    div2level_selector = "td:nth-of-type(9)"
    detail_selector = "td:nth-of-type(11) > a"
    soup = BeautifulSoup(htmldoc)
    rows = soup.select(row_selector)
    problems = []
    for r in rows:
        print(r)
    return problems

class ProblemArchiveParser:
    url = 'http://community.topcoder.com/tc?module=ProblemArchive&sc=0&sd=asc&er=10000'
    root_selector = """html > body > table:nth-of-type(1) > tbody > tr > td:nth-of-type(3) >
    table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td > form > table:nth-of-type(4) > tbody > tr"""
    name_selector = "td:nth-of-type(2) > a"
    contest_selector = "td:nth-of-type(3) > a"
    date_selector = "td:nth-of-type(4)"
    categories_selector = "td:nth-of-type(6)"
    div1level_elector = "td:nth-of-type(7)"
    div2level_selector = "td:nth-of-type(9)"
    detail_selector = "td:nth-of-type(11) > a"
    start_index = 3
    step = 1

    def parse(htmldoc):
        soup = BeautifulSoup(htmldoc)
        root = soup.select(ProblemArchiveParser.root_selector)
        pass

class FileArchiveParser:
    pass

class ProblemStatementParser:
    pass

class ProblemSolutionParser:
    pass

class ProblemDetailParser:
    pass

if __name__ == '__main__':
    from filegrabber import FileGrabber
    grabber = FileGrabber()
    url = 'http://community.topcoder.com/tc?module=ProblemArchive&sc=0&sd=asc&er=10000'
    htmldoc = grabber.grab(url)
    soup = BeautifulSoup(htmldoc)
    with open('temp.html', 'w') as f:
        f.write(soup.prettify())
    parse_problem_archive(htmldoc=htmldoc)

