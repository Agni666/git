def pobierz_wyrazy(nazwa):
    """
    Funkcja pobiera z pliku tekst i dzieli go na wyrazy.
    Zwraca liste wyrazow.
    """
    lista = []
    plik = open(nazwa,'r')
    calosc = plik.read()
    calosc = calosc.replace(".","")
    calosc = calosc.replace(",","")
    calosc = calosc.replace(";","")
    calosc = calosc.replace("?","")
    calosc = calosc.replace("!","")
    calosc = calosc.replace("\n","")
    calosc = calosc.split(" ")
    for wyraz in calosc:
        lista.append(wyraz)
    return lista
    
def histogram(nazwa):
    """
    Funkcja rysuje histogram licznosci liter w wyrazie.
    Pobiera nazwe pliku z ktorego pobiera tekst.
    Zwraca na ekran hitogram.
    """
    if type(nazwa) == str:
	listawyrazow = pobierz_wyrazy(nazwa)
    if type(nazwa) == list:
	listawyrazow = nazwa
    slownik = {}
    wynik = ""
    for wyraz in listawyrazow:
        dlugosc = len(wyraz)
        if dlugosc in slownik:
            slownik[dlugosc] += 1
        else:
            slownik[dlugosc] = 1
    for i in slownik.keys():
	for znak in range(slownik[i]):
	    wynik += "#"
        print i, wynik
	wynik = ""

print histogram('tekst.txt')
