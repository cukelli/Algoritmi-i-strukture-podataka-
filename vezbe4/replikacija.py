def replikacija(broj, ponavljanja):

    if (ponavljanja == 1):
        return [broj]
    else:
        return [broj] + replikacija(broj, ponavljanja - 1)


print(replikacija(2, 3))
