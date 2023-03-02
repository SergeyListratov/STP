from collections import namedtuple
from datetime import datetime

with open('meetings.csv', 'r', encoding='UTF-8') as file:
    title, *meet_list1 = file.read().split()
Meeting = namedtuple('Meeting', 'name,meeting')
# meet_list2 = []
# for i in meet_list1:
#     lst = i.split(",")
#     meeting = Meeting(f'{lst[0]} {lst[1]}', datetime.strptime(f'{lst[2]} {lst[3]}', '%d.%m.%Y %H:%M'))
#     meet_list2.append(meeting)

meet_list2 = [Meeting(f'{i.split(",")[0]} {i.split(",")[1]}', datetime.strptime(f'{i.split(",")[2]} {i.split(",")[3]}', '%d.%m.%Y %H:%M')) for i in meet_list1]
for i in sorted(meet_list2, key=lambda j: j[1]):
    print(i.name)
