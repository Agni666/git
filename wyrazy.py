text = open('tekst.txt').read()
text.replace(",","")
text.replace("/n","")
text=text.split(' ',)
print text

lista=[]
for j in range (30):
	lista.append(0)

for i in text:
	lista[len(i)]+=1

print lista
