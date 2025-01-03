def generate_parenthesis(n):
    stack = []
    res = []

    def bactrack(openN, closedN):
        if openN==closedN==n:
            res.append("".join(stack))
            return
        if openN <n:
            stack.append("(")
            bactrack(openN+1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            bactrack(openN, closedN+1)
            stack.pop()
    bactrack(0,0)
    return res
    

print(generate_parenthesis(3))