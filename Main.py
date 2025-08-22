from Personagem import Personagem
from CriarPersonagem import CriarPersonagem
from Raca import Raca
from Atributos import Atributos

# Criação dos objetos
p = Personagem()
r = Raca()
a = Atributos()


p.nome = input("Digite seu nome: ")
p.idade = int(input("Digite sua idade: "))


print("\nEscolha sua raça:")
print("1 = Elfo \n2 = Anão \n3 = Humano \n4 = Gnomo \n5 = Meio Elfo \n6 = Halfing")
escolha = int(input("Escolha uma Raça: "))
r.escolhaRaca(escolha)


print(f"\n{p.nome}, {p.idade} anos, Raça: {r.raca}")


print("\nEscolha o estilo de geração de atributos:")
print("1 - Estilo Clássico (3d6 em ordem)")
print("2 - Estilo Aventureiro (3d6 com distribuição livre)")
print("3 - Estilo Heroico (4d6, descarta menor, com distribuição livre)")

estilo = input("Digite o número do estilo desejado: ")

print("\n--- Rolando os dados para gerar atributos ---")


if estilo == "1":
    a.gerar_clássico()
elif estilo == "2":
    a.gerar_aventureiro()
elif estilo == "3":
    a.gerar_heroico()
else:
    print("Estilo inválido. Gerando atributos com estilo clássico por padrão.")
    a.gerar_clássico()


print("\n--- Seus atributos finais ---")
for nome, valor in a.AtributosRandom.items():
    desc = a.descricao(nome, valor)
    print(f"{nome.capitalize()}: {valor} → {desc}")
