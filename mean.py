def mean(s):
    sa = s.split(', ')
    c = 0
    mean = 0
    while len(sa) > c:
        sa[c] = float(sa[c])
        mean = mean + sa[c]
        c += 1
    return mean