cal = input("enter the calculation / for divide")
calarray = [*cal]
calArray = 0
calarray.
if "x" in cal:
    calarray = "".join(calarray)
    calArray = cal.split("x")
    ans = int(calArray[0]) * int(calArray[1])
    print(ans)
if "/" in cal:
    calarray = "".join(calarray)
    calArray = cal.split("x")
    ans = int(calArray[0]) / int(calArray[1])
    print(ans)
if "-" in cal:
    calarray = "".join(calarray)
    calArray = cal.split("x")
    ans = int(calArray[0]) - int(calArray[1])
    print(ans)
if "+" in cal:
    calarray = "".join(calarray)
    calArray = cal.split("+")
    ans = int(calArray[0])+int(calArray[1])
    print(ans)
