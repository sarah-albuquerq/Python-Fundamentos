# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print("\n Selecione o número da operação desejada"
"\n 1- Soma"
"\n 2- Subtração"
"\n 3- Multiplicação")

operacao = int(input("Digite sua opção"))

n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))


def soma(n1,n2):
    return n1+n2

def sub (n1,n2):
    return n1-n2

def multip (n1,n2):
    return n1*n2

def divis (n1,n2):
    return n1/n2

if operacao == 1:
    print('%s + %r = ' %(n1,n2), soma(n1,n2))
elif operacao == 2:
    print('%s - %r = ' %(n1,n2), sub(n1,n2))
elif operacao == 3:
    print('%s x %r = ' %(n1,n2), multip(n1,n2))
elif operacao == 4:
    print('%s / %r = ' %(n1,n2), divis(n1,n2))
else:
    print('Opção inválida!')