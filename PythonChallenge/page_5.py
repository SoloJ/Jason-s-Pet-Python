import pickle

word_list = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/PythonChallenge/page_5.txt").read()
data = pickle.load(open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/PythonChallenge/page_5.txt"))
print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])




