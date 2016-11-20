#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


MY_DICT = {
    'A': 1.0,
    'B': 0.9,
    'C': 0.8,
    'D': 0.7,
    'F': 0.6
    }


def get_score_summary(my_arg1):
    """This function does some file operations.

    Args:
        my_arg(string): Passed argument opens file.

    Returns:
        dict: Dictionary, keyed by boro and number of restaurants whose value is
        a tuple with the number of restaurateurs per boro (who have scores), and
        the average score (as a float) for that boro.

    Examples:

    >>>get_score_summary('inspection_results.csv')
    {'BRONX': (156, 0.9762820512820516), 'BROOKLYN': (417, 0.9745803357314144),
    'STATEN ISLAND': (46, 0.9804347826086955), 'MANHATTAN': (748, 0.977139037433
    1529), 'QUEENS': (414, 0.9719806763285015)}
    """
    my_arg = open(my_arg1, 'r')
    my_dict1 = {}

    for line in open('inspection_results.csv'):
        line = my_arg.readline()[1:]
        parts = line.split(',')
        if parts[10] != 'P' and parts[10] != '':
            my_dict1.update({parts[0]: (parts[1], parts[10])})

    my_arg.close()

    bk_cn = 0
    bk_gr = 0

    qn_cn = 0
    qn_gr = 0

    mn_cn = 0
    mn_gr = 0

    si_cn = 0
    si_gr = 0

    bx_cn = 0
    bx_gr = 0
    my_dict2 = {}
    for _, value in my_dict1.iteritems():
        if value[0] == 'BROOKLYN':
            bk_cn += 1
            bk_gr += MY_DICT[value[1]]
            my_dict2[value[0]] = (bk_cn, bk_gr/bk_cn)
        if value[0] == 'QUEENS':
            qn_cn += 1
            qn_gr += MY_DICT[value[1]]
            my_dict2[value[0]] = (qn_cn, qn_gr/qn_cn)
        if value[0] == 'STATEN ISLAND':
            si_cn += 1
            si_gr += MY_DICT[value[1]]
            my_dict2[value[0]] = (si_cn, si_gr/si_cn)
        if value[0] == 'MANHATTAN':
            mn_cn += 1
            mn_gr += MY_DICT[value[1]]
            my_dict2[value[0]] = (mn_cn, mn_gr/mn_cn)
        if value[0] == 'BRONX':
            bx_cn += 1
            bx_gr += MY_DICT[value[1]]
            my_dict2[value[0]] = (bx_cn, bx_gr/bx_cn)
    return my_dict2
