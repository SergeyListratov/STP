from zipfile import ZipFile
import json


def data_v(size: int):
    if size < 1024:
        return f'{size} {"B"}'
    elif 1024 <= size < 1048576:
        return f'{round(size / 1024)} {"KB"}'
    elif 1048576 <= size < 1073741824:
        return f'{round(size / (1024 * 1024))} {"MB"}'
    elif 1073741824 <= size < 1073741824:
        d = round(size / (1024 * 1024 * 1024))
        return f'{round(size / (1024 * 1024 * 1024))} {"GB"}'


if __name__ == '__main__':
    info_list, list_set = [], {'', 0}
    with ZipFile('desktop.zip', 'r') as zip_f:
        info_l = [i.filename.split('/') + [i.file_size] for i in zip_f.infolist()]
    for i in info_l:
        for j in range(len(i) - 1):
            if i[j] not in list_set:
                if i[j + 1] != 0 and type(i[j + 1]) == int:
                    print(f'{" " * 2 * j}{i[j]} {data_v(i[j + 1])}')
                else:
                    print(f'{" " * 2 * j}{i[j]}')
                list_set.add(i[j])
