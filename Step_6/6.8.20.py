from collections import Counter


if __name__ == '__main__':
    c_dict, total = dict(), 0
    b_dict = Counter(input().split())
    print(b_dict)
    for i in range(int(input())):
        b = input().split()
        if b[0] in c_dict:
            c_dict[b[0]].append(int(b[1]))
        else:
            c_dict[b[0]] = [int(b[1])]
    for k, v in b_dict.items():
        if k in c_dict:
            if len(c_dict[k]) >= v:
                total += sum(c_dict[k][:v])
            else:
                total += sum(c_dict[k][:len(c_dict[k])])

    print(total)
