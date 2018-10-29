
import collections

page_source = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/PythonChallenge/page_source.txt")
contents_of_page_source = page_source.read()
check_this = list(contents_of_page_source)
cnt = collections.OrderedDict()
cnt[ collections.Counter(contents_of_page_source)
ocnt = collections.Counter()
n = 0