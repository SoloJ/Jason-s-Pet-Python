

web_page = open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/PythonChallenge/page3_text.txt")
page_text = web_page.read()
page_text = page_text.replace("\n","")
size_table = len(page_text)
page_text_snippits = [" "] * size_table

n = 0
c = 0
d = 7
while d < len(page_text):
    page_text_snippits[c] = page_text[c:d]
    c = c + 1
    d = d + 1
    n = n + 1

n = 0
counter = 0

while n < size_table-7:
    check_string = str(page_text_snippits[n])
    if all((check_string[-3:].isupper(), check_string[:-4].isupper(), check_string[3].islower())):
        check1 = page_text_snippits[n - 1]
        check2 = page_text_snippits[n + 1]
        if all((check1[0].islower(), check2[6].islower())):
            print(check_string[3])
            n = n + 1
        else:
            n = n + 1
    else:
        n = n + 1






print(n)
z = 0