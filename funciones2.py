#!/usr/bin/env python
# coding: utf-8

# In[26]:


def tabla_de_multiplicar(num):
    for i in range(1, 11):
        print(num, "*", i, "=",i*num)
num = int(input("Ingresa la tabla que quieres ver: "))
resultado = tabla_de_multiplicar(num)
print (resultado)


# In[18]:


def cadena():
    return "curso de python"
print (cadena())


# In[20]:


n = 5
def funcion():
    print (n)
funcion()


# In[22]:


def suma(a,b):
    return a+b
a = int(input("Primer numero de la suma: "))
b = int(input("Segundo numero de la suma: "))
resultado = suma(a,b)
print(resultado)


# In[28]:


def tabla_de_multiplicar(num):
    for i in range(1, 11):
        print(num, "*", i, "=",i*num)
num = int(input("Ingresa la tabla que quieres ver: "))
print (tabla_de_multiplicar(num))


# In[36]:


numeros = [3,7,9,5,8,3,7,12]#hacemos una lista 
def separar_numeros(lista):
    lista.sort()#sort ordena la lista 
    pares = []#nueva lista
    impares = []#nueva lista 
    for i in lista: #verificar uno por uno par o impar
        if i % 2 == 0: 
            pares.append(i)#si es par se almacena gracias a append
        else:
            impares.append(i)#si es impar se almacena gracias a append
    return pares,impares
pares,impares = separar_numeros(numeros)
print ("Los numeros pares son: ", pares)
print ("Los numeros impares son: ", impares)


# In[ ]:




