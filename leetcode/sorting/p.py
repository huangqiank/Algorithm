def merge_interval(inputs):
    if not inputs:
        return
    if len(inputs) == 1:
        return inputs[0]
    if len(inputs) == 0:
        return
    inputs = sorted(inputs, key=lambda key: (key[0], key[1]))
    for i in range(1, len(inputs)):
        combine(inputs[i],res)
    return res
def combine(interval,res):
    last = res[-1]
    if last[1] >= interval[0]:
        new = [last[0],max(interval[1],last[1])]
        res.pop()
        res.append(new)
    else:
        res.append(interval)





