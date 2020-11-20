'''
Created on Jan 22, 2018

@author: qiankunhuang
'''


def max_product(n):
    dp = [1 for i in range(n + 1)]
    for i in range(2, n + 1, 1):
        global_max = 1
        for j in range(0, i, 1):
            global_max = max(global_max, j * max(i - j, dp[i - j]))
        dp[i] = global_max
    return dp[n]


def fib(n):
    res = [1, 1, 1]
    if n <= 2:
        return 1
    for i in range(3, n):
        res[n] = res[n - 2] + res[n - 1]
    return res[n]


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def max_product(n):
    dp = [1 for i in range(n + 1)]
    for i in range(2, n + 1, 1):
        global_max = 1
        for j in range(0, i, 1):
            global_max = max(global_max, j * (max(i - j, dp[i - j])))
        dp[i] = global_max
    return dp[n - 1]


def climb_stair(n):
    dp = [1 for i in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1, 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def coin_change(coins, n):
    max = float("inf")
    dp = [0] + [max] * n
    for i in range(1, n + 1):
        global_num = max
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != max:
                global_num = min(global_num, dp[i - coin] + 1)
        dp[i] = global_num
    if dp[n] == max:
        return -1
    return dp[n]


def dictionary_word(a, b):
    n = len(a) + 1
    dp = [False for i in range(n)]
    dp[0] = True
    for j in range(n):
        for i in range(j):
            if dp[i] and a[i:j] in b:
                dp[j] = True
    return dp[n - 1]


def jump_game(a):
    if a is None or len(a) == 0:
        return 1
    n = len(a)
    dp = [False for i in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(a[i] + 1):
            if i + j >= n or dp[i + j]:
                dp[i] = True
                break
    return dp[0]





def longest_asc_array(lst):
    if not lst or len(lst) == 0:
        return 0
    n = len(lst)
    dp = [1 for i in range(n)]
    global_max = 1
    for i in range(1, n, 1):
        if lst[i] > lst[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            global_max = max(global_max, dp[i-1])
    return max(global_max, dp[n - 1])

lst = [1, 2, 3, 45, 0, -1, 2, 1, -4]

print(longest_asc_array(lst))