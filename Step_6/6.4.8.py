import copy
from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    i = 0
    if by_values:
        i = 1
    ordered_list = sorted(ordered_dict.items(), key=lambda v: v[i])
    for i in ordered_list:
        # ordered_dict.pop(i[0])
        ordered_dict.move_to_end(i[0])


if __name__ == '__main__':
    data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
    custom_sort(data, by_values=True)
    print(data)





    # data = OrderedDict({'Law & Order': 1990, 'The Practice': 1997, 'Six Feet Under': 2001, 'Joan of Arcadia': 2003,
    #                     'The West Wing': 1999, 'Deadwood': 2004, 'The Sopranos': 1999, 'Boston Legal': 2004, 'ER': 1994,
    #                     'Friday Night Lights': 2006, '24': 2001, 'Heroes': 2006, 'Lost': 2004, 'Dexter': 2006,
    #                     'Damages': 2007, 'Big Love': 2006, 'House': 2004, 'Downton Abbey': 2010, "Grey's Anatomy": 2005,
    #                     'Homeland': 2011, 'Breaking Bad': 2008, 'Game of Thrones': 2011,
    #                     'CSI: Crime Scene Investigations': 2000, 'Boardwalk Empire': 2010, 'True Blood': 2008,
    #                     'House of Cards': 2013, 'True Detective': 2014})

    # data.sorted_keys = lambda reverse = False: sorted(data.keys(), reverse=1) if reverse == True else sorted(data.keys())
    # data.sorted_values = lambda reverse = False: sorted(data.values(), reverse=1) if reverse == True else sorted(data.values())
    #
    # print(data.sorted_keys())
    # print(data.sorted_values())




