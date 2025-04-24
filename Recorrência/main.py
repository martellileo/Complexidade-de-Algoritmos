# Recorrencia linear simples
def fibonnaciLinearSimples(n):
    if n <= 1:
        return n
    return fibonnaciLinearSimples(n-1) + fibonnaciLinearSimples(n-2)

def linearSimples(n):
    if n == 0:
        return 0
    return 2 * linearSimples(n - 1) + 1

# Teste
for i in range(10):
    print(f"fibonnaci({i}) = {fibonnaciLinearSimples(i)}")

for i in range(10):
    print(f"T({i}) = {linearSimples(i)}")
