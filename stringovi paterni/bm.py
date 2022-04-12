def boyer_moore(T, P):
    n = len(T)
    m = len(P)
    last = {}
    # abacab
    for i in range(m):
        last[P[i]] = i
    i = m-1
    j = m-1
    while i < n:
        if T[i] == P[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        else:
            l = last.get(T[i], -1)
            i += m - min(j, l+1)
            j = m - j
    return -1


print(boyer_moore("trllababa", "la"))
