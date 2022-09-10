

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

def inv_matriz(a):
    resultado = []
    

v = [[5,3], [8,2]]
w = [[3,4], [9,3]]

A = [[(5,3), (8,2)], [(4,8), (6,9)], [(2,5), (3,1)]]
B = [[(6,4), (4,7)], [(8,3), (9,8)], [(7,1), (9,6)]]
add_matrices(A,B);