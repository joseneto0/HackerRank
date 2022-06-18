x = int(input())
y = int(input())
z = int(input())
n = int(input())
lista = []
lados = []
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
            if X+Y+Z != n:
                lados = [X,Y,Z];
                lista.append(lados)
print(lista)