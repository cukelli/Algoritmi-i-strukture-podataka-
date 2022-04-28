



def obrni_cifre(integer):
    if integer < 0:
        return '-' + str(abs(integer))[::-1]
    else:
        return str(integer)[::-1]

print(obrni_cifre(123))
print(obrni_cifre(-234))



def nule_na_kraj(niz):
    if 0 in niz:
        niz.remove(0)
        niz.append(0)
    return niz 

print(nule_na_kraj([1,4,0,2,4,0]))


def proveri_duplikate(niz):
    if len(niz) == len(set(niz)):
        return "Nema dupikata"
    else:
        return "Ima duplikate"

print(proveri_duplikate([1,1,3,3,5,3]))
print(proveri_duplikate([2,4,5,1]))


def obrni_recenicu(recenica):
    splituj = recenica.split(" ")
    obrni = ' '.join(reversed(splituj))

    print(obrni)

obrni_recenicu("Zovem se Mirko")



def prebroj_samoglasnike(string):
     lista_slova = []
     brojac = 0 
     samoglasnici = "aeiouAEIOU"
     for slovo in string:
         if slovo in samoglasnici:
             brojac+=1 
             lista_slova.append(slovo)
     print(brojac)
     print(list(set(lista_slova)))

prebroj_samoglasnike("Anastasija")



def suma_cifara(string):
    suma = 0
    
    for i in string:
        if i.isdigit():
            suma += int(i)
        else:
            pass 
    
    return suma 

print(suma_cifara("123aw"))



def najmanji(br):
    min = br[0]
    for i in range(len(br)):
        if br[i] < min:
            min = br[i]
    
    return min 

print(najmanji([2,4,5]))