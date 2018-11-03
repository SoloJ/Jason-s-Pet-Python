
import os
from sets import Set
import zipfile

n = str(90052)


list_keeper = []
z=0
files = os.listdir("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/PythonChallenge/channel")
file_strip = [s.strip(".txt") for s in files]

while z<908:
    word_list = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/PythonChallenge/channel/" + n + ".txt").read()
    word_list_List = word_list.split()
    n = word_list_List[3]
    list_keeper.append(n)
    print(word_list)
    z = z+1

diff_list = set(file_strip).difference(list_keeper)
my_file = zipfile.ZipFile("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/PythonChallenge/channel.zip")
iguess = my_file.comment
