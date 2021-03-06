#!/usr/bin/python
"""
Binary search that returns the item that is just greater if 
it does not equal.
"""
def binSearch(nums, b, e, k):
    while b < e:
        mid = b+(e-b)/2
        if k <= nums[mid]:
            e = mid
        else:
            b = mid+1
    return b

def binSearch(nums):
     beg, end = 0, len(nums)
     while beg < end:
         mid = beg + (end-beg)/2
         if nums[mid] < target:
             beg = mid+1
         else:
             end = mid
     return beg

def test1():
    nums = [2, 3, 4, 8, 9, 10]
    print(binSearch(nums, 0, len(nums), 7))

if __name__ == '__main__':
    test1()
