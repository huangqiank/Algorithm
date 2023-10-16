# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 注意:
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
# 示例 1 :
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
## a[i-1] > a[i] 就删除a[i-1]
## 1234
## 4321


class Solution:
    def removeKdigits(self, num, k):
        num = [int(i) for i in num]
        n = len(num)
        res = [num[0]]
        count = 0
        for i in range(1, n):
            while len(res) > 0 and res[-1] > num[i] and count < k:
                res.pop()
                count += 1
            res.append(num[i])
        res = [str(i) for i in res]
        ans = "".join(res).lstrip("0")
        dif = k - count
        if dif > 0 and len(ans) <= dif:
            return 0
        m = len(ans)
        if dif > 0 and m > dif:
            ans = ans[0:m - dif]
        if dif == 0 and len(ans) == 0:
            return 0
        return str(ans)


s = Solution()
print(s.removeKdigits("10", 1))


class Solution23:
    def expand(self, s: str):
        s = s.replace(",", "")
        self.res = []
        self.dfs(0, "", s)
        return sorted(self.res)

    def dfs(self, index, path, s):
        if index == len(s):
            self.res.append(path)
            return
        if s[index] == "{":
            stack = []
            index += 1
            while index < len(s) and s[index] != "}":
                stack.append(s[index])
                index += 1
            for w in stack:
                self.dfs(index + 1, path + w, s)
        else:
            self.dfs(index + 1, path + s[index], s)


class Solution3:
    def bicycleYard(self, position, terrain, obstacle):
        self.n = len(terrain)
        self.m = len(terrain[0])
        self.terrain = terrain
        self.obstacle = obstacle
        x, y = position
        speed = 1
        self.res = []
        self.visited = set()
        self.dfs(x, y, speed)
        self.res = sorted(self.res)
        return self.res

    def dfs(self, x, y, speed):
        self.visited.add((x, y, speed))
        for (new_x, new_y) in [(x + speed, y), (x - speed, y), (x, y + speed), (x, y - speed)]:
            if new_x < 0 or new_x >= self.n or new_y < 0 or new_y >= self.m:
                continue
            new_speed = speed + self.terrain[x][y] - self.terrain[new_x][new_y] - self.obstacle[new_x][new_y]
            if new_speed <= 0:
                continue
            if new_speed == 1:
                self.res.append([new_x, new_y])
            if (new_x, new_y, new_speed) in self.visited:
                continue
            self.dfs(new_x, new_y, new_speed)

terrain =[[48,39,83,65,33,18,50,5,14],[46,95,62,1,67,84,71,76,49],[6,73,12,51,54,5,90,83,10],[1,8,42,63,91,3,5,63,66],[56,62,32,25,5,39,9,82,1],[62,4,51,94,3,78,0,28,84],[89,40,35,54,11,28,54,29,23],[2,22,55,99,9,48,27,71,2]]
obstacle =[[21,46,15,28,49,39,12,12,1],[39,10,23,38,14,41,40,1,6],[1,12,27,27,8,28,0,45,26],[29,53,37,33,18,1,17,40,1],[31,18,48,40,30,29,48,37,11],[27,26,37,42,11,30,3,31,24],[44,25,10,41,28,19,8,15,34],[46,36,47,4,5,37,40,37,13]]
s = Solution3()
print(s.bicycleYard([1,1],terrain,obstacle))



class Solution4:
    def bicycleYard(self, position, terrain, obstacle) :
        n, m = len(terrain), len(terrain[0])
        a, b = position[0], position[1]
        sl = []
        visited = set()

        def dfs(i,j,v):
            if (i,j,v) in visited:
                return
            visited.add((i,j,v))
            if v == 1:
                sl.append([i,j])
            for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                x = i + dx
                y = j + dy
                if x < 0 or x > n-1 or y < 0 or y > m-1:
                    continue
                after_v = v + terrain[i][j] - terrain[x][y] - obstacle[x][y]
                if after_v > 0:
                    if x==1 and y == 1:
                        print(i,j,after_v)
                    dfs(x,y, after_v)
        dfs(a,b,1)
        sl.remove([a,b])
        return list(sl)
s = Solution4()
print(s.bicycleYard([1,1],terrain,obstacle))

##      (1,1)-->(2,1) --->(3,1) -- > (3,0)