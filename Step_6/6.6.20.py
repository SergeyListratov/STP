import copy
from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    i = 1
    if by_values:
        i = 0
    ordered_list = sorted(ordered_dict.items(), key=lambda v: v[i])
    for i in ordered_list:
        # ordered_dict.pop(i[0])
        ordered_dict.move_to_end(i[0])