#1
def fahrenheit_para_celsius(f):
    c = (f - 32)/1.8
    print("Resultado: %d" % c)

def celsius_para_fahrenheit(c):
    f = (c*1.8)+32
    print("Resultado: %d" % f)

#2
def primo(numero):
    contador = 0
    for elemento in range (1,numero+1):
        if (numero % elemento == 0):
            contador = contador + 1
    if (contador==2):
        return True
    else:
        return False


#3
def concatenarLista(lista):
    new = []
    for each_item in lista:
        if isinstance(each_item,list):
            for elemento in each_item:
                #concatenarLista(each_item)
                new.append(elemento)
        else:
            new.append(each_item)
    return new
            
    
        
#4
def inverterFrase(frase):
    str = frase
    str = str[::-1]
    print ("Frase invertida: " + str)


    
print("QUESTÃO 01")
a = float(input("Converter F para C: "))
fahrenheit_para_celsius(a)
b = float(input("Converter C para F: "))
celsius_para_fahrenheit(b)

print("\n")

print("QUESTÃO 02")
numero = int(input("Digite um numero inteiro e verifique se ele é numero primo: "))
primo(numero)
if (primo(numero)==True):
    print("%d é primo\n"%numero)
else:
    print ("%d não é primo\n"%numero)
print("NUMEROS PRIMOS DE 1 A 100")
for elemento in range(1,100):
    if (primo(elemento)==True):
        print("%d é primo"%elemento)

print("\n")

print("QUESTÃO 03")
lista = [[2,5,4],7,9,[7,4],['oi','ola']]
print (concatenarLista(lista))

print("\n")

print("QUESTÃO 04")
#inverterFrase("ola tudo bem")
frase = input ("Digite uma frase: ")
inverterFrase(frase)


