def pobierz_wyrazy(nazwa):
    lista = []
    plik = open(nazwa,'r')
    calosc = plik.read()
    calosc = calosc.split(" ")
    for wyraz in calosc:
        lista.append(wyraz)
    return lista

def histogram(nazwa):
    slownik = {}
    listawyrazow = pobierz_wyrazy(nazwa)
    for wyraz in listawyrazow:
        dlugosc = len(wyraz)
        if dlugosc in slownik:
            slownik[dlugosc] += 1
        else:
            slownik[dlugosc] = 1
    print slownik
    for i in slownik.keys():
        print i, slownik[i]
        
histogram('wyrazy.txt')