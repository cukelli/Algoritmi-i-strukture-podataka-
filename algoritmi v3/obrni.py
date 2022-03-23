def main():
    recenice = input("Unesite recenicu: ")
    obrni_recenicu(recenice)


def obrni_recenicu(recenica):

    splituj = recenica.split(" ")

    nova_recena = list(reversed(splituj))
    print((" ".join(nova_recena)))


main()
