def factorial(n):
    # base case
    if n==0 or n==1:
        return 1
    result= n * factorial(n-1)
    print(result)
    return result



print(factorial(5))