n = int(input())
estudantes = {}
for i in range(n):
    a, *lista = input().split()
    notas = list(map(float, lista))
    estudantes[a] = notas
opcao = input()
media = sum(estudantes[opcao]) / len(estudantes[opcao])
print(f'{media:.2f}')