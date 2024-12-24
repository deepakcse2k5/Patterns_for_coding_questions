def happy_number(num):
    slow = num
    fast = square_of_num(num)

    while fast!=1 and fast!= slow:
        slow = square_of_num(num)
        fast = square_of_num(square_of_num(num))
    if fast==1:
        return True
    return False



def square_of_num(num):
    result = 0
    while (num>0):
        rem = num%10
        num_suqare = rem* rem
        result +=num_suqare
        num = num//10
    return result


print(happy_number(25))