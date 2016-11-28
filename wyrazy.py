text = open('tekst.txt').read()
text.split(' ',)
print text

lista=[]
for j in range (30):
	lista.append(0)

for i in text:
	lista[len(i)]+=1

print lista

def pobierz_wyrazy(nazwa):
    plik = open(nazwa,'r')
    for wyraz in plik.readlines():
        print(wyraz)
    plik.close()

pobierz_wyrazy('wyrazy.txt')
