# Recorrencia linear simples
def linear1(n):
    if n == 0:
        return 0
    return linear1(n-1) + 7

def linear2(n):
    if n == 0:
        return 1
    return 2 * linear2(n-1)

# Recorrencia binaria
def binaria1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return binaria1(n-1) + 2*binaria1(n-2)

def binaria2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    return 4*binaria2(n-1) - 4*binaria2(n-2)

# Divisao e conquista
def potencia(base, expoente):
    if expoente == 0:
        return 1
    half = potencia(base, expoente // 2)
    if expoente % 2 == 0:
        return half * half
    else:
        return base * half * half

def contar(lista):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return 1
    meio = len(lista) // 2
    return contar(lista[:meio]) + contar(lista[meio:])


# Linear com Deslocamento
def deslocamento1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return deslocamento1(n-2) + 3

def deslocamento2(n):
    if n < 3:
        return 1
    return 2 * deslocamento2(n-3)

# Multiplas dependencias
def multiplas1(n):
    if n in (0, 1, 2):
        return 1
    return multiplas1(n-1) + multiplas1(n-2) + multiplas1(n-3)

def multiplas2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    return 2*multiplas2(n-1) - multiplas2(n-3)
