'''
Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno
'''

lista1=[1,2,3,4,5,6,7,8,9]
lista2=[1,3,5,6,7,9]
def intersect (lista1,lista2):
    comunes=[]
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                comunes.append(lista1[i])
    return comunes

print(intersect(lista1, lista2))
                