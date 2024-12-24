from typing import List


def dailyTemperatures( temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp, index

        for index, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stack_val, stack_index = stack.pop()
                res[stack_index] = index- stack_index
            stack.append((val, index))
        return res

print(dailyTemperatures([30,38,30,36,35,40,28]))