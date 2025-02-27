pilha = []
def push(pilha, item): 
    pilha.append(item)

def peek(pilha):
    if pilha:
        return pilha[-1]
    return None

print(pilha)
push(pilha, 'A')
push(pilha, 'B')

print(pilha)
pilha.pop()
print(peek(pilha))