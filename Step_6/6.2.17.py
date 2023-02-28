import string

bbb = string.ascii_lowercase
cc = dict(zip(string.ascii_lowercase, input()))
str = input()
tbl = str.lower().maketrans(cc)
print(str.lower().translate(tbl))