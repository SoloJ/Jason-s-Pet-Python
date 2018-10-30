
import urllib
n = 87890
counter = 0

while counter < 100:
    text = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" +str(n)).read()
    split_text = text.split()
    for s in split_text:
        if s.isdigit():
            n = s
        else:
            print(n)
    counter = counter + 1
print (s)
print (" ".join(split_text))



