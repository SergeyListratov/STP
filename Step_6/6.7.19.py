from collections import Counter


def t_cost(st: str) -> int:
    s = 0
    for i in st:
        if i != ' ':
            s += ord(i)
    return s


if __name__ == '__main__':
    sort_list = []
    with open('pythonzen.txt', 'r', encoding='UTF=8') as file:
        # sort_list = list(filter(lambda s: s.isalpha(), file.read()))
        for s in file.read():
            if s.isalpha():
                sort_list.append(s.lower())
    print(*map(lambda i: f'{i[0]}: {i[1]}', sorted(Counter(sort_list).items())), sep='\n')

#     shop_list = 'рубашка,футболка,футболка,брюки,футболка,сырный соус,рубашка,носки,рубашка'
#     shop_dict = Counter(sorted(shop_list.split(',')))
#     max_len = len(sorted(shop_dict.keys(), key=lambda j: len(j), reverse=1)[0])
#     print(*map(lambda i: f'{i[0]}{(max_len - len(i[0])) * " "}: {t_cost(i[0])} UC x {i[1]} = {t_cost(i[0]) * i[1]} UC', shop_dict.items()), sep='\n')
