#!/usr/bin/python
"""
Given a string S and a string T, find the minimum window in S which will contain all
the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.

#76
REDDO: must get slide window first try
review
"""

def minWindowSlideWin(s, t):
    """
    68.8% performance
    """
    mp = [0]*128
    cnt = 0
    set_t = set(list(t))
    win_s = len(s)+1
    get_idx = lambda c: ord(c)
    for c in t: mp[get_idx(c)] += 1
    left, right = 0, 0
    hd = 0

    for right in range(len(s)):
        if s[right] in set_t:
            mp[get_idx(s[right])] -= 1
            if mp[get_idx(s[right])] >= 0:
                cnt += 1

        while cnt == len(t):
            if right-left+1 < win_s:
                win_s = right-left + 1
                hd = left

            if s[left] in set_t:
                mp[get_idx(s[left])] += 1
                if mp[get_idx(s[left])] > 0:
                    cnt -= 1

            left += 1

    return '' if win_s == len(s)+1 else s[hd:hd+win_s]

def minWindowSlideWin_r(s, t):
    map = [0]*128
    count = 0
    set_t = set(list(t))
    for i in t:
        map[ord(i)] += 1
        count += 1

    beg = 0
    min_len_s = s + 'Z'

    for end in range(len(s)):
        v = s[end]
        map[ord(v)] -= 1

        if map[ord(v)] >= 0:
            count -= 1

        while count == 0:
            temp_s = s[beg:end+1]
            min_len_s = temp_s if len(temp_s) < len(min_len_s) else min_len_s

            if s[beg] in set_t:
                map[ord(s[beg])] += 1
                if map[ord(s[beg])] > 0:
                    count += 1

            beg += 1

    return min_len_s if min_len_s != s + 'Z' else ''

def minWindow_r2(s, arr):
    """
    re-implement v2. 88.8% acceptance
    """
    thresh_hist = {}
    hist = {}
    res = s + '1'
    count, total = 0, 0

    # populate thresh_hist
    for ch in arr:
        thresh_hist[ch] = thresh_hist.get(ch, 0) + 1
        hist[ch] = 0
        total += 1

    beg, end = 0, -1
    while end < len(s):
        # increase the end to cover everything
        if count < total:
            end += 1
            if end == len(s):
                break

            ch = s[end]
            if ch not in hist: continue
                
            hist[ch] += 1
            # increase count, if hist element <= thresh_hist
            if hist[ch] <= thresh_hist[ch]:
                count += 1
        else: 
            # as long as total == count, take min string
            res = s[beg:end+1] if (end-beg+1) < len(res) else res
            ch = s[beg]
            if ch in hist:
                hist[ch] -= 1
                # decrease count, if hist element < thresh_hist [done]
                if hist[ch] < thresh_hist[ch]:
                    count -= 1
            beg += 1

    return res if res != s+'1' else ''

def minWindow(s, t):
    """
    TLE with 267/268 accepted.
    """
    min_win_s = len(s)
    win_subs = ''
    w_dic = {}
    for i in range(len(s)-len(t)+1):
        for c in t: w_dic[c] = w_dic.get(c, 0) + 1

        for j in range(min_win_s):
            if i+j < len(s) and s[i+j] in w_dic:
                w_dic[s[i+j]] -= 1
                if w_dic[s[i+j]] == 0: del w_dic[s[i+j]]

            if not w_dic:
                min_win_s = j+1
                win_subs = s[i:i+j+1]
                break

        w_dic.clear()

    return win_subs

def test1():
    s = 'ADOBECODEBANCDDD'
    t = 'ABC'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print(minWindowSlideWin_r(s, t))
    print('----------------')

def test2():
    s = 'ADOBECODEBANCDDD'
    t = 'XYZ'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print(minWindowSlideWin_r(s, t))
    print('----------------')

def test3():
    s = ''
    t = 'ABC'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print(minWindowSlideWin_r(s, t))
    print('----------------')

def test4():
    s = ''
    t = ''
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print(minWindowSlideWin_r(s, t))
    print('----------------')

def test5():
    s = 'a'
    t = 'a'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print(minWindowSlideWin_r(s, t))
    print('----------------')

def test6():
    s = 'aZ'
    t = 'aZ'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print(minWindowSlideWin_r(s, t))
    print('----------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
