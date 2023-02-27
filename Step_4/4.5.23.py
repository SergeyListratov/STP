from zipfile import ZipFile
import json

def foo():
    pass


if __name__ == '__main__':
    with ZipFile('data.zip', 'r') as zip_f:
        zip_f.printdir()
