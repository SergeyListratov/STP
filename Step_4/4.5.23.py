from zipfile import ZipFile
import json


def data_v(dat):
    pass


if __name__ == '__main__':
    info_list, list_set = [], {'', 0}
    with ZipFile('test.zip', 'r') as zip_f:
        info_l = [i.filename.split('/') + [i.file_size] for i in zip_f.infolist()]
    print(info_l)
    for i in info_l:
        for j in range(len(i) - 1):
            if i[j] not in list_set:
                if i[j + 1] != 0 and type(i[j + 1]) == int:
                    print(f'{" " * 2 * j}{i[j]} {i[j + 1]}')
                else:
                    print(f'{" " * 2 * j}{i[j]}')
                list_set.add(i[j])
