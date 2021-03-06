#!/usr/bin/python
"""
Given two sorted lists containing transaction ids.
beg_list, end_list
the goal here is to make the content of two lists equal.
most of the content in both lists are the same except for a few ones.

Real life experience question from ELK stack at Tascent
"""
def makeListsEqual(l1, l2):
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            del l1[i]
        else:
            del l2[j]

    if len(l1) < len(l2):
        l2 = l2[:len(l1)]
    elif len(l2) < len(l1):
        l1 = l1[:len(l2)]

    print(len(l1))
    print(len(l2))

def test1():
    l1 = [1, 2, 3, 5, 7, 9, 11]
    l2 = [1, 2, 4, 5, 9]
    makeListsEqual(l1, l2)
    print('----------')

def test2():
    l1 = [1, 2, 3, 5]
    l2 = [1, 2, 4, 5, 9]
    makeListsEqual(l1, l2)
    print('----------')

def test3():
    l1 = [3, 5, 11]
    l2 = [1, 3, 4, 5, 9]
    makeListsEqual(l1, l2)
    print('----------')

def test4():
    l1 = []
    l2 = [1, 2, 3, 4]
    makeListsEqual(l1, l2)

def test5():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 10, 11]
    l2 = [1, 9, 9, 9, 10]
    makeListsEqual(l1, l2)

def test6():
    l1 = read_to_list('start_tid.txt')
    l2 = read_to_list('end_tid.txt')
    makeListsEqual(l1, l2)

def read_to_list(f_n):
    with open(f_n, 'r') as f:
        res = [int(line.strip()) for line in f]
    return res

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
