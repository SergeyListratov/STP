from collections import defaultdict


def wins(game_list: list) -> dict:
    # g_l = []
    # g_l.extend(game_list)
    g_dict = defaultdict(set)
    for i in game_list:
        g_dict[i[0]].add(i[1])
    return g_dict


def flip_dict(dict_to_flip: dict) -> dict:
    fl_dict = defaultdict(list)
    for k, v in dict_to_flip.items():
        for u in v:
            fl_dict[u].append(k)
    return fl_dict


def best_sender(mess: list, send: list) -> str:
    mess_dict = defaultdict(int)
    mess_len = list(map(lambda i: len(i.split()), mess))
    for j in range(len(send)):
        mess_dict[send[j]] += mess_len[j]
    mess_dict = dict(sorted(mess_dict.items(), reverse=1))
    mess_dict = dict(sorted(mess_dict.items(), key=lambda k: k[1], reverse=1))
    return list(mess_dict.keys()).pop(0)


if __name__ == '__main__':
    messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
    senders = ['Bob', 'Charlie']

    print(best_sender(messages, senders))





