
def generate_parenthesis(n):
    # edge case
    if n==0:
        return []
    combinations = []
    paren = []
    back_track(n,combinations, paren, open_paren_count=0, closed_paren_count=0)
    return combinations

def back_track(n,combinations, paren, open_paren_count, closed_paren_count):

    if open_paren_count>=n and closed_paren_count>=n:
        combinations.append(''.join(paren))

    if open_paren_count<n:
        paren.append("(")
        back_track(n,combinations,paren,open_paren_count+1, closed_paren_count)
        paren.pop()
    if closed_paren_count< open_paren_count:
        paren.append(")")
        back_track(n, combinations,paren, open_paren_count, closed_paren_count+1)
        paren.pop()


print(generate_parenthesis(3))

# Time complexity
# As visualized in the slides above, it’s easier to understand the problem by creating a tree.Given a tree with branching of b and a maximum depth of
# m, the maximum number of nodes in this tree would be the following:
# 1 + b + b**2+...+b**(m−1)

# This is the sum of a geometric sequence, which evaluates to the following:(1−b**m)/(1−b)

# So, we can say that time complexity is O(b**m).For our problem here, the following is true:

# There is a branching of 2 because we only add an opening or a closing brace at each step.

# There is a maximum depth of 2n,because the length of the output is the sum of n opening and n closing parentheses.

# This leads us to a time complexity of O(2**(2n), that is, O(4**n).

# Space complexity
# The space complexity of this solution is O(n), since the maximum size of the stack is 2n.

