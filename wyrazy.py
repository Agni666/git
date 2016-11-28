def pobierz_wyrazy(nazwa):
    lista = []
    plik = open(nazwa,'r')
    calosc = plik.read()
    calosc = calosc.split(" ")
    for wyraz in calosc:
        print wyraz
        
pobierz_wyrazy('wyrazy.txt')