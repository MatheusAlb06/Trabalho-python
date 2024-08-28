contador = 0

def incrementar_contador():
    global contador
    contador += 1
    print(contador)
    mensagem = 'exercicio2'

incrementar_contador()
print(mensagem)