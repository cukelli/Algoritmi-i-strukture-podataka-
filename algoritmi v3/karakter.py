def main():
    recenica = input("Unesite recenicu ")
    solution(recenica)


def solution(recenica):

    karakter = input("Koji zelite da izbacite?")

    if karakter in recenica:
        print(recenica.replace(karakter, ''))


main()
