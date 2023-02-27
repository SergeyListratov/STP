from zipfile import ZipFile
import json


def is_correct_json(st):
    try:
        d = json.load(st)
        return d
    except json.decoder.JSONDecodeError:
        return {'team': ''}


def is_correct_json_plus(zp, nm):
    try:
        with zp.open(nm) as f:
            return json.loads(f.read().decode('UTF-8'))
    except:
        return {'team': ''}


if __name__ == '__main__':
    with ZipFile('data.zip', 'r') as zip_f:
        name_list = [name for name in zip_f.namelist() if name[-5:] == '.json']
        play_list = [f'{i["first_name"]} {i["last_name"]}' for n in name_list for i in [is_correct_json_plus(zip_f, n)] if i['team'] == 'Arsenal' ]
        print(*sorted(play_list), sep='\n')

from zipfile import ZipFile
# import json

# def jsloads(z, n):
#     try:
#         with z.open(n) as f:
#             return json.loads(f.read().decode('utf-8'))
#     except:
#         return {'team': ''}
#
# with ZipFile('data.zip') as z:
#     names = [n for n in z.namelist() if n[-5:] == '.json']
#     n = {i['first_name'] + ' ' + i['last_name'] for n in names for i in [jsloads(z, n)] if i['team'] == 'Arsenal'}
#     print(*sorted(n), sep='\n')


######################################
# otvet=[]
# with zp('data.zip') as zip_file:
#     for i in zip_file.infolist():
#         with zip_file.open(i) as file:
#             try:
#                 data=json.loads(file.read().decode('utf-8'))
#                 if data['team']=='Arsenal':
#                     otvet.append((data['first_name'],data['last_name']))
#             except: pass
# for i in sorted(otvet):
#     print(f'{i[0]} {i[1]}')

####################################

# with ZipFile('data.zip') as zip_file:
#     lst = []
#     for i in zip_file.namelist():
#         with zip_file.open(i) as json_file:
#             try: lst.append(json.load(json_file))
#             except: ...
#     [print(i['first_name'], i['last_name'])
#      for i in sorted(filter(lambda x: x['team'] == 'Arsenal', lst),
#                      key=lambda x: (x['first_name'], x['last_name']))]

#############
#
# import json as js
#
# with __import__('zipfile').ZipFile('data.zip') as zf:
#     l = []
#     for i in zf.infolist():
#         if not i.is_dir() and i.filename.endswith('.json'):
#             zf.extract(i)
#             try:
#                 with open(i.filename, encoding='utf-8') as file:
#                     p = js.load(file)
#                     if p['team'] == 'Arsenal':
#                         l.append((p['first_name'], p['last_name']))
#             except:
#                 continue
#
# [print(*i) for i in sorted(l)]
