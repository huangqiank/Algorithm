# 在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：
# "G"：直走 1 个单位
# "L"：左转 90 度
# "R"：右转 90 度
# 机器人按顺序执行指令 instructions，并一直重复它们。
# 只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
# 示例 1：
# 输入："GGLLGG"
# 输出：true
# 解释：
# 机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
# 重复这些指令，机器人将保持在以原点为中心，2 为半径的环中进行移动。


l_dir = {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 0)}
r_dir = {(1, 0), (0, -1), (-1, 0), (0, 1), (1, 0)}


class Solution:
    def isRobotBounded(self, instructions):
        l_dir = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
        r_dir = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
        x, y = 0, 0
        cur_state = (0, 1)
        for i in instructions * 4:
            if i == "G":
                x += cur_state[0]
                y += cur_state[1]
            if i == "L":
                cur_state = l_dir[cur_state]

            if i == "R":
                cur_state = r_dir[cur_state]

        if x == 0 and y == 0:
            return True
        return False


s = Solution()
print(s.isRobotBounded("GLRLLGLL"))
