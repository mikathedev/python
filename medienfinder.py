def medein(i):

    sa = i.split(", ")
    c = 0
    ans = 0
    # convert to string
    while len(sa) > c:
        sa[c] = int(sa[c])
        c += 1
    sa.sort()

    # if is even
    if (len(sa) / 2).is_integer():
        len2 = (len(sa) / 2)
        ans = (sa[int(len2 - 0.5)] + sa[int(len2 + 0.5)]) / 2

    # if is not even
    else:
        x = int(((len(sa) / 2)+0.5)-1)
        ans = sa[x]

    return ans
