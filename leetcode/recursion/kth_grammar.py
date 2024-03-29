# 第K个语法符号
# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
# 例子:
# 输入: N = 1, K = 1
# 输出: 0

# 输入: N = 2, K = 1
# 输出: 0

# 输入: N = 2, K = 2
# 输出: 1

# 输入: N = 4, K = 5
# 输出: 1

#0
#01
#0110
##01101001
class Solution {
public:
    int kthGrammar(int N, int K) {
        if(N==1&&K==1) return 0;
        return kthGrammar(N-1,(K+1)/2)==(K%2);
    }
};

