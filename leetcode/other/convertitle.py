##168. Excel表列名称
#给定一个正整数，返回它在 Excel 表中相对应的列名称。
#例如，
#    1 -> A
#    2 -> B
#    3 -> C
#    ...
#    26 -> Z
#    27 -> AA
#    28 -> AB
#    ...
#示例 1:
#输入: 1
#输出: "A"
##只需要注意1 - A而不是0 - A
##①让除数减一，那么余数自然就少一，原来余 1 的变成余 0，以此类推(详细见下表)。
#核心代码 `let remain = (n - 1) % 26;`
class Solution123411:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n:
            n -= 1
            # ASCII码转大写字符 并且左加
            s = chr(65 + n % 26) + s
            n //= 26
        return s


## 2 3 4
##4
##2*2