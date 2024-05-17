import random
import string

def gerar_codigo(codigos_gerados):
    letras_numeros = string.ascii_uppercase + string.digits

    while True:
        parte1 = ''.join(random.choices(letras_numeros, k=6))
        parte2 = ''.join(random.choices(letras_numeros, k=6))
        parte3 = ''.join(random.choices(letras_numeros, k=6))

        codigo = f"{parte1}-{parte2}-{parte3}"

        if codigo not in codigos_gerados:
            return codigo

def gerar_codigos(quantidade):
    codigos_gerados = set()
    while len(codigos_gerados) < quantidade:
        codigos_gerados.add(gerar_codigo(codigos_gerados))
    return codigos_gerados

print ("bem vindo ao: (welcome to:)")
print("--------------------------------------------------------------")
print("░█░█░███░█░█")
print("░██░░██░░███")
print("░█░█░███░░█░")
print("░████░█████'░████░████░██░░░██░░'░████'░░████░░██░░░█░")
print("░█░░░░░░█░░░█░░░░░█░░█░█░█░█░█░░░█░░░░'░░█░░░░░█░█░░█░")
print("░░██░░░░█░░░███░'░████░█░░█░░█░░░█░░██░'░███░░░█░░█░█░")
print("░░░░█░░░█░░░█░░░░░█░░█░█░░░░░█░░░█░░░█'░░█░░░░░█░░█░█░")
print("░████░░░█░░'░████░█░░█░█░░░░░█░░░░███░░'░████░░█░░░██░")
print("by sr.raposo on viniciusrinaldi")
print("--------------------------------------------------------------")

print("how many key steam you want generate?")
quantidade = int(input("Quantas key steam você gostaria de gerar? "))
codigos_gerados = gerar_codigos(quantidade)

for codigo in codigos_gerados:
    print(codigo)
    
if quantidade == 1:
    print(quantidade, "key foi gerada com sucesso!")
else:
    print(quantidade, "key foram geradas com sucesso!")
