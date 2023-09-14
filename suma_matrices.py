#este script suma  2 matrices normales y de numpy
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [9, 5, 4],
    [3, 2, 1]
]

for k in range(3):
    #suma la primera fila de las matrices A y B
    for i in range(3):
        suma=A[0][i]+B[0][i]
        print(suma)


""""
#suma la primera fila de las matrices A y B
for i in range(3):
    suma=A[0][i]+B[0][i]
    print(suma)

#suma la primera fila de las matrices A y B
for i in range(3):
    suma=A[0][i]+B[0][i]
    print(suma)

#suma la primera fila de las matrices A y B
for i in range(3):
    suma=A[0][i]+B[0][i]
    print(suma)
"""