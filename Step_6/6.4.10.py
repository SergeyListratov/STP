from collections import namedtuple
import pickle


def my_foo():
    pass


if __name__ == '__main__':
    Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
    with open('data.pkl', 'rb') as file:
        animal_list = pickle.load(file)
    for i in animal_list:
        print()
        for k, v in zip(Animal._fields, i):
            print(f'{k}: {v}')
