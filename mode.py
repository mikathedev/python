import statistics
def mode(i):
    c = 0
    while len(i) > c:
        i[c] = int(i[c])
        c += 1

    return(statistics.mode(i))
