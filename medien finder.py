s = input("commas and spaces inbetewn")
sa = s.split(", ")
c = 0
ans = 0
# convert to string
while len(sa) > c:
    sa[c] = int(sa[c])
    c += 1
sa.sort()
print(len(sa) / 2)
# if is even
if (len(sa) / 2).is_integer():
    len2 = (len(sa) / 2)
    ans = (sa[int(len2 - 0.5)] + sa[int(len2 + 0.5)]) / 2
    print("no int")

# if is not even
else:
    ans = sa[int((len(sa) / 2)+0.5)]
    print(sa[int((len(sa) / 2)+0.5)])
print(sa)
print(ans)
