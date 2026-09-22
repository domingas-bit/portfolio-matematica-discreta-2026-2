print("Portfólio de Programação Matemática")
print("Nome: Domingas Farias Moura Neta")
print("Matrícula: 2612082008")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino")
print("Professora: Cristiane Loesch")
print()

print("Atividade 1 - Teoria dos Conjuntos")
print()

a = set(input("Digite os elementos de A separados por espaço: ").split())
b = set(input("Digite os elementos de B separados por espaço: ").split())

print()
print("A =", a)
print("B =", b)

print()
print("União =", a | b)
print("Interseção =", a & b)
print("A - B =", a - b)
print("B - A =", b - a)

print()
print("Cardinalidade de A =", len(a))
print("Cardinalidade de B =", len(b))
print("Cardinalidade da União =", len(a | b))
print("Cardinalidade da Interseção =", len(a & b))

lista_a = list(a)
partes_a = []

for i in range(2 ** len(lista_a)):
    sub = []
    for j in range(len(lista_a)):
        if i & (1 << j):
            sub.append(lista_a[j])
    partes_a.append(sub)

lista_b = list(b)
partes_b = []

for i in range(2 ** len(lista_b)):
    sub = []
    for j in range(len(lista_b)):
        if i & (1 << j):
            sub.append(lista_b[j])
    partes_b.append(sub)

print()
print("Conjunto das partes de A:")
print(partes_a)

print()
print("Conjunto das partes de B:")
print(partes_b)

print()
print("Cardinalidade P(A) =", len(partes_a))
print("Cardinalidade P(B) =", len(partes_b))

print()
print("Exemplo de partição de A:")
print([list(a)])

produto = []

for x in a:
    for y in b:
        produto.append((x, y))

print()
print("Produto Cartesiano A x B =")
print(produto)

print()
print("A está contido em B?", a.issubset(b))
print("B está contido em A?", b.issubset(a))

input("\\nPressione Enter para sair...")
