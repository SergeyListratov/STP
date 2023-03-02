from collections import namedtuple


def my_foo():
    pass


if __name__ == '__main__':
    Game = namedtuple('Game', 'name developer publisher')

    ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])

    e = ExtendedGame(1, 2, 3, 4, 5)
    print(ExtendedGame._fields)

