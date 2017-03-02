#1
#MANEIRA 1
print('QUESTAO 01')
lista = [1, 2, 5, 78, 9]
print ('LISTA =',lista)

#MANEIRA 2
'''
lista = []
for inicio in range (5):
    lista.append(int(input('Digite um numero:')))
print ('LISTA =',lista)
''' 
print('\n')

#2
#MANEIRA 1
print('QUESTAO 02')
lista = [1, 2, 5, 78, 9, 48, 75, 26, 3, 100]
lista.reverse()
print ('ORDEM INVERSA =',lista)

#MANEIRA 2
'''
lista = []
for inicio in range (10):
    lista.append(int(input('Digite um numero:')))
lista.reverse()
print ('LISTA =',lista)
'''
print('\n')

#3
print('QUESTAO 03')
#MANEIRA 1
lista = [10, 9.5, 9, 8]
soma = 0
for inicio in lista:
    print (inicio)
    soma = soma + inicio
media = soma / len(lista)
print ('MEDIA =',media)

#MANEIRA 2
'''
lista = []
media = soma = 0
for inicio in range(4):
    lista.append(float(input('Digite nota:')))
for inicio in lista:
    print (inicio)
    soma = soma + inicio
media = soma / len(lista)
print ('SOMA =',soma)
print ('MEDIA =',media)
'''
print('\n')

#4
#MANEIRA 1
print('QUESTAO 04')
lista = ['w','t','u','m','a','y','p','o','b','e']
vogais = 'aeiou'
contador = 0
for inicio in lista:
    if inicio not in vogais:
        print (inicio)
        contador = contador + 1
print ('TOTAL DE CONSOANTES =',contador)

#MANEIRA 2
'''
lista = []
contador = 0
for inicio in range(10):
    lista.append(input('Digite caracter:'))
for inicio in lista:
    if inicio not in vogais:
        print (inicio)
        contador = contador + 1
print ('TOTAL DE CONSOANTES =',contador)
'''
print('\n')

#5
#MANEIRA 1
print('QUESTAO 05')
numeros = [2,4,5,8,96,35,78,41,25,698,52,17,100,256,968,632,547,852,301,605]
impar = []
par = []
for inicio in numeros:
    if (inicio % 2 == 0):
        par.append(inicio)
    else:
        impar.append(inicio)
print('LISTA =',numeros,'\nPAR =',par,'\nIMPAR =',impar)

#MANEIRA 2
'''
numeros = []
impar = []
par = []
for inicio in range(20):
    numeros.append(int(input('Digite um numero:')))
for inicio in numeros:
    if (inicio % 2 == 0):
        par.append(inicio)
    else:
        impar.append(inicio)
print('LISTA =',numeros,'\nPAR =',par,'\nIMPAR =',impar)
'''
print('\n')

#6
'''
print('QUESTAO 06')
lista = []
nota = media = count = 0
for inicio in range(10):
    print('Aluno (%d)'%(inicio+1))
    media = 0
    for inicio in range (4):
        nota = (float(input('Nota %d = '%(inicio+1))))
        media = media + nota
    media = media/4
    lista.append(media)
for inicio in lista:
    print ("MEDIAS = %.2f"%inicio)
    if (inicio>=7):
        count+=1
print('QUANTIDADE DE ALUNOS COM MEDIA IGUAL OU MAIOR QUE 7 =',count)

print('\n')
'''
#7
print('QUESTAO 07')
lista1 = [1, 20, 10, 48, 7, 59, 638, 85, 72, 93]
lista2 = [24, 69, 874, 32, 64, 51, 28, 60, 37, 2]
lista3 = []
for inicio,inicio2 in zip(lista1,lista2):
    lista3.append(inicio)
    lista3.append(inicio2)
print ("LISTA 1:",lista1)
print ("LISTA 2:",lista2)
print ("LISTA INTERCALADA:",lista3)

print('\n')

#8

print('QUESTAO 08')
temperaturas = []
numero = 1
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print('Entre com as temperaturas em cada mes')
media = 0
for inicio in range(12):
    temperaturas.append(float(input('%d - %s: ' %((inicio+1),(mes[inicio])))))
    media += temperaturas[inicio]
media = media/len(temperaturas)
print("MEDIA = %.2f"%media)
for inicio in range(len(temperaturas)):
    if (temperaturas[inicio] > media):
        print('%d - %s - %.2f' %((numero),(mes[inicio]),(temperaturas[inicio])))
        numero+=1

print('\n')

#9
print('QUESTAO 09')
perguntas=["Telefonou para a vitima?","Esteve no local do crime?","Mora perto da vitima?","Devia para a vitima?","Ja trabalhou com a vitima?"]
contador = 0
for inicio in perguntas:
    resposta = input(str(inicio) + " - S ou N: ")
    if (resposta == 'S'):
        contador+=1
print("Classificação sobre a participação da pessoa no crime")
if (contador==2):
    print("Resultado: %d - Suspeita"%contador)
elif (contador==3 or contador==4):
    print("Resultado: %d - Cumplice"%contador)
elif (contador==5):
    print("Resultado: %d - Assassino"%contador)
elif (contador<2):
    print("Resultado: %d - Inocente"%contador)

print('\n')


#10
print('QUESTAO 10')
notas=[]
nota=soma=contador=0
while True:
    nota =(float(input("Digite nota: ")))
    if (nota==-1):
        break
    notas.append(nota)
print("A - Quantidade de valores que foram lidos: ",len(notas))
print("B - Valores na ordem em que foram informados: ",notas)
print("C - Valores na ordem inversa à que foram informados, um abaixo do outro:")
notas.reverse()
for inicio in notas:
    print(inicio)
    soma+=inicio
print("D - Soma dos valores: ",soma)
media=soma/len(notas)
print("D - Média dos valores: ",media)
for inicio in notas:
    if (inicio>media):
        contador+=1
print("E - Quantidade de valores acima da média calculada: ",contador)
contador = 0
for inicio in notas:
    if (inicio<7):
        contador+=1
print("F - Quantidade de valores abaixo de sete: ",contador)
print("Fim")
