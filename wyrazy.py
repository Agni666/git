def pobierz_wyrazy(nazwa):
    plik = open(nazwa,'r')
    for wyraz in plik.readlines():
        print(wyraz)
    plik.close()
        
pobierz_wyrazy('wyrazy.txt')