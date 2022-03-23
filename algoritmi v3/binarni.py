def main():
    string = input("Unesite string")
    solution(string)


def solution(string):
    for char in string:

        if (char != '0' and char != '1'):
            print("Nije binarni")
            break
        else:
            print("Jeste binarni!")
            break


main()
