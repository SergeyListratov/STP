import pickle

f, *data = list(map(str.strip, open(0)))
with open(f, 'rb') as bf:
    func = pickle.load(bf)
print(func(*data))

