# Programa_que_determina_si_una_lista_tiene_elementos_repetidos

def sin_repetidos(lista):
    #Si_el_largo_de_la_lista_es_igual_al_largo_del_conjunto_de_la_lista,_no_hay_repetidos
    if len(lista) == len(set(lista)):
        print("La lista no tiene elementos repetidos")
    else:
        print("La lista tiene elementos repetidos")

mi_lista = [1, 2, 3, 4, 5]
sin_repetidos(mi_lista)





#Programa_que_determina_si_en_una_lista_existe_una_cadena_con_dos_o_más_vocales
def cadena_con_dos_vocales(lista):
    vocales = "aeiouAEIOU"
    for cadena in lista:
        contador = 0
        for letra in cadena:
            if letra in vocales:
                contador += 1
        if contador >= 2:
            print("Existe:", cadena)
            return
    print("No existe")

lista_palabras = ["sol", "mar", "flor", "cielo"]
cadena_con_dos_vocales(lista_palabras)






#Desarrolle_un_programa_que_dada_dos_listas_determiene_que_elementos_tiene_la_primera_lista_que_no_tenga_la_segunda

def elementos_unicos(lista1, lista2):
    #Recorre_los_elementos_de_la_primera_lista_y_guarda_los_que_no_están_en_la_segunda
    resultado = []
    for elemento in lista1:
        if elemento not in lista2:
            resultado.append(elemento)
    return resultado
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 6]

unicos = elementos_unicos(lista1, lista2)

print("Elementos que están en la primera lista y no en la segunda:", unicos)




#Desarrollar_un_algoritmo_que_calcule_el_promedio_de_un_arreglo_de_reales

def promedio_arreglo(numeros):
    if len(numeros) == 0:
        return 0
    suma = 0
    for n in numeros:
        suma += n
    promedio = suma / len(numeros)
    return promedio

arreglo = [3.5, 4.0, 5.5, 2.0]
print("El promedio es:", promedio_arreglo(arreglo))
