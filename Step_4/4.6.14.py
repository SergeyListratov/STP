import pickle


def filter_dump(filename: str, objects: list, typename: type):
    sort_obj = list(filter(lambda i: type(i) == typename, objects))
    with open(filename, 'wb') as f:
        pickle.dump(sort_obj, f)


def pik_print(st: str):
    with open(st, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)

print(pik_print('numbers.pkl'))
