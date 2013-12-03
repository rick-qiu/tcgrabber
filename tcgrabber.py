__author__ = 'Rick Qiu'

from filegrabber import FileGrabber
import parser

url = 'http://community.topcoder.com/tc?module=ProblemArchive&sc=0&sd=asc&er=10000'

parser.parse_problem_archive("<html><head></head><body></body></html>")
grabber = FileGrabber()
htmldoc = grabber.grab(url)
parser.parse_problem_archive(htmldoc=htmldoc)
