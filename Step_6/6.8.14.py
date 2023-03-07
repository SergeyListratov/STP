from collections import Counter, defaultdict
import sys

def my_foo():
    pass


if __name__ == '__main__':
    st = 'Не сможет больше мальчик дотронуться до солнца'
    # # st1 = [i for i in sys.stdin]
    # print(Counter(st.lower().split()))
    # len_list = sorted([len(i) for i in st.split()], reverse=1)
    # print(len_list)
    l = defaultdict(int)
    for i in [len(i) for i in st.split()]:
        l[i] += 1
    for k, v in sorted(l.items(), key=lambda j: i[1]):
        print(f'Слов длины {k}: {v}')

    len_list = Counter([len(i) for i in st.split()]).elements()
    for k, v in sorted(Counter(len_list).items(), key=lambda j: j[1]):
        print(f'Слов длины {k}: {v}', sep='\n')
    # print(sorted([i[0] for i in Counter(st.lower().split()).most_common() if Counter(st.split()).most_common()[0][1] == i[1]], reverse=1)[0])
    # print(sorted([i[0] for i in Counter(st.lower().split()).most_common() if Counter(st.lower().split()).most_common()[0][1] == i[1]], reverse=1)[0])



