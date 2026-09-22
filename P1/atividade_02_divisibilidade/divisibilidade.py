print("Portfólio de Programação Matemática")
print("Nome: Domingas Farias Moura Neta")
print("Matrícula: 2612082008")
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno: Matutino")
print("Professora: Cristiane Loesch")
print()

print("Atividade 2 - Divisibilidade, MDC e MMC")
print()

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print()
print("DIV =", a // b)
print("MOD =", a % b)

print()
print("Passo a passo do Algoritmo de Euclides:")

x = a
y = b

while y != 0:
    resto = x % y
    print(x, "=", y, "*", x // y, "+", resto)
    x = y
    y = resto

mdc = x

print()
print("MDC =", mdc)

mmc = (a * b) // mdc

print("MMC =", mmc)

input("\\nPressione Enter para sair...")
