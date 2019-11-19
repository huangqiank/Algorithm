##Three stones are on a number line at positions a, b, and c.
##Each turn, you pick up a stone at an endpoint(ie., either the lowest or highest position
##stone), and move it to an unoccupied position between those endpoints.Formally,
##let say the stones are currently at positions x, y, z with x < y < z.
##You pick up the stone at either position x or position z,
##and move that stone to an integer position k, with x < k < z and k != y.
##The game ends when you cannot make any more moves, ie.the stones are in consecutive positions. When the game
##ends, what is the minimum and maximum number of moves that you could have made?  Return the
##answer as an length 2 array: answer = [minimum_moves, maximum_moves]
##
##Example1
##Input: a = 1, b = 2, c = 5
##Output: [1, 2]
##Explanation: Move the stone
##from 5 to 3, or move the
##stone from 5 to 4 to 3.
##Example2
##Input: a = 4, b = 3, c = 2
##Output: [0, 0]
##Explanation: We cannot make any moves.
##Example3
##Input: a = 3, b = 5, c = 1
##Output: [1, 2]
##Explanation: Move the stone from 1 to 4;
##or move the stone from 1 to 2 to 4.
##Note:
##1 <= a <= 100
##1 <= b <= 100
##1 <= c <= 100
##a != b, b != c, c != a


def numMovesStones(a, b, c):
    s = [a, b, c]
    max_num = max(s)
    min_num = min(s)
    mid_num = sum(s) - max_num - min_num
    max_swap = max_num - min_num - 2
    if max_num - mid_num <= 2 or mid_num - min_num <= 2:
        min_swap = 1
    if max_num - mid_num == 1 and mid_num - min_num == 1:
        min_swap = 0
    if max_num - mid_num > 2 and mid_num - min_num > 2:
        min_swap = 2
    return [min_swap, max_swap]
a = 1
b = 2
c = 5
print(numMovesStones(a,b,c))