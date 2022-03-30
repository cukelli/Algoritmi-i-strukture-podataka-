def recursiveLength(String):
    if String == '':
        return 0

    return 1 + recursiveLength(String[1:])


print(recursiveLength("Pera Peric"))
