import statistics
def mode(i):
    c = 0
    i = i.split(", ")
    while len(i) > c:
        i[c] = float(i[c])
        c += 1

    return statistics.mode(i)
