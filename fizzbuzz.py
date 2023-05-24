count = 0
while count <= 100:
    x3 = count/3
    x5 = count / 5
    if x3.is_integer() and x5.is_integer():
        print("FizzBuzz")
        count = count+1
    elif x3.is_integer():
        print("Fizz")
        count = count+1
    elif x5.is_integer():
        print("Buzz")
        count = count+1
    else:
        print(count)
        count = count+1

