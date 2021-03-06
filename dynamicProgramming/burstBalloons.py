#!/usr/bin/python
"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
on it represented by array nums. You are asked to burst all the balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then
becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <= n <= 500, 0 <= nums[i] <= 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

#312
REDDO: great problem
"""
def bb(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [x[:] for x in [[0]*n]*n]

    for k in range(2, n):
        for left in range(n-k):
            right = left+k
            for i in range(left+1, right):
                dp[left][right] = max(dp[left][right], \
                    nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right])

    return dp[0][n-1]

def bb_dfs_r(nums):
    """
    13/67 accepted
    """
    if not nums: return 0
    max_val = 0
    for i in range(len(nums)):
        lhs = 1 if i == 0 else nums[i-1]
        rhs = 1 if i == len(nums)-1 else nums[i+1]
        max_val = max(max_val, \
            lhs*nums[i]*rhs + bb_dfs_r(nums[:i] + nums[i+1:]))

    return max_val

def bb_dfs_r2(nums, l, r):
    """
    13/67 accepted
    """
    if l > r: return 0
    max_val = 0
    for i in range(l, r+1):
        lhs = 1 if i == 0 else nums[i-1]
        rhs = 1 if i == len(nums)-1 else nums[i+1]
        max_val = max(max_val, \
            lhs*nums[i]*rhs + bb_dfs_r2(nums, l, i-1) + bb_dfs_r2(nums, i+1, r))

    return max_val

def test1():
    nums = [3, 1, 5, 8]
    print(bb(nums))
    print(bb_dfs_r(nums))

if __name__ == '__main__':
    test1()
