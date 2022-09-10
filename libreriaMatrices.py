

import libreria as lib

def add_vector(a,b):
    "Realiza la suma entre vectores"
    r = []
    for j in range(len(a)-1):
        r.append(lib.sumai(a[j],b[j]))
    return r

def inv_add(a):
    inverso = []
    for i in range(len(a)-1):
        inverso.append(lib.inverso(a[i]))
    return inverso

def mult_esc_vect(vector,a):
    resultado = []
    for i in range(len(vector)):
        resultado.append(lib.multii((a,0),vector[i]))
    return resultado

def add_matrices(a,b):
    resultado = []
    for i in range(len(a)-1):
        resultado.append(add_vector(a,b))
    print(resultado)

def mult_esc_matriz(matriz,a):
    resultado = []
    for i in range(len(matriz)):
        resultado.append(mult_esc_vect((matriz,a)))
    return resultado

