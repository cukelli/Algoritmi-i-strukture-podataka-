def stepen(broj, eksponent):

    if (eksponent == 1):
        return broj

    elif (eksponent == 0):
        return(1)

    else:
        return stepen(broj, eksponent - 1) * broj


print(stepen(5, 3))
