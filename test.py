def find(heights):
    n = len(heights)
    if n == 0:
        return []
    if n == 1:
        return [0]
    stack = []
    res = []
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(0)
        else:
            res.append(stack[-1])
        stack.append(i)
    return res[::-1]
## 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