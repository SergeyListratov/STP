from zipfile import ZipFile
import json

def foo():
    pass


if __name__ == '__main__':
    info_list = []
    with ZipFile('test.zip', 'r') as zip_f:
        info_l = [i.filename.split('/') + [i.file_size] for i in zip_f.infolist()]
    print(info_l)
    for i in info_l: