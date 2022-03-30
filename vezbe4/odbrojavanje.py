def odbrojavanje(broj):

    if (broj != 0):
        odbrojavanje(broj - 1)
        print(broj)

    else:
        print(0)


odbrojavanje(5)
