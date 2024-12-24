def function_three():
    print("Three")


def function_two():
    function_three()
    print("Two")


def function_one():
    function_two()
    print("One")


function_one()
