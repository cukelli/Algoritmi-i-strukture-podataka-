niz = [25, 11, 7, 75, 56]


max = niz[0]


for i in range(0, len(niz)):
    if(niz[i] > max):
        max = niz[i]

print("Najveci element je: " + str(max))
