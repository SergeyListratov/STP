import string

# a, b = input(), input()

aa = string.ascii_lowercase
bb = list(map(int, range(len(aa))))
cc = dict(zip(bb, aa))
print(cc)