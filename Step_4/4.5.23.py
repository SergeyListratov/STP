from zipfile import ZipFile
import json

def foo():
    pass


if __name__ == '__main__':
    info_list, list_set = [], {'', 0}
    with ZipFile('test.zip', 'r') as zip_f:
        info_l = [i.filename.split('/') + [i.file_size] for i in zip_f.infolist()]
    print(info_l)
    for i in info_l:
        for j in range(len(i)):
            if i[j] not in list_set:
                print(f'{" " * 2 * j}{i[j]}')
                list_set.add(i[j])
