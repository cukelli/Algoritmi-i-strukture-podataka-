def fail(P):
    m = len(P)
    failed = [0] * m
    k = 0
    i = 1
    while i < m:
        if P[i] == P[k]:
            failed[i] = k + 1
            k += 1
            i += 1
        elif k > 0:
            k = failed[k-1]
        else:
            i += 1
    return failed  # atzo


def kmp(T, P):
    n = len(T)
    m = len(P)
    failed = fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j-k
            j += 1
            k += 1
        elif k > 0:
            k = failed[k-1]
        else:
            j += 1
    return -1


print(kmp("Pera Peric", "Peric"))
