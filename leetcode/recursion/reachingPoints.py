
##从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。
# 给定一个起点 (sx, sy) 和一个终点 (tx, ty)，如果通过一系列的转换可以从起点到达终点，则返回 True ，否则返回 False。
# 示例:
# 输入: sx = 1, sy = 1, tx = 3, ty = 5
# 输出: True
# 解释:
# 可以通过以下一系列转换从起点转换到终点：
##(1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)

class Solution14135():
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx >tx or sy>ty:
            return False
        if sx == tx and (ty-sy) %sx ==0 :
            return True
        if sy == ty and (tx-sx) %sy ==0 :
            return True
        if tx>ty:
            return self.reachingPoints(sx,sy,tx%ty,ty)
        return self.reachingPoints(sx,sy,tx,ty%tx)



s = Solution14135()
print(s.reachingPoints(3, 3, 12, 9))
