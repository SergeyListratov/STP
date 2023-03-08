from collections import Counter


def my_foo():
    pass


if __name__ == '__main__':
    words_dict = Counter(sorted(input().lower().split(), reverse=1))
    print(*[i[0] for i in words_dict.most_common()[::-1] if i[1] == words_dict.most_common()[-1][1]], sep=', ')


