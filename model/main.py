from personagem import Personagem
from model.criar_personagem import CriarPersonagem
from raca import Raca
from atributos import Atributos
from classe import Classe
import os

p = Personagem()
r = Raca()
a = Atributos()
c = Classe()



p.nome = input("Digite seu nome: ")
p.idade = int(input("Digite sua idade: "))
os.system('cls' if os.name == 'nt' else 'clear')


print("\nEscolha sua raça:")
print("1 = Elfo \n2 = Anão \n3 = Humano \n4 = Gnomo \n5 = Meio Elfo \n6 = Halfing")
escolha = int(input("Escolha uma Raça: "))
os.system('cls' if os.name == 'nt' else 'clear')
print("1 = Guerreiro \n2 = Mago \n3 = Ladrão \n")
classe = int(input("Escolha uma Classe: "))
r.escolhaRaca(escolha)
r.atributosRaca(p.idade)
c.escolhaClasse(classe)
os.system('cls' if os.name == 'nt' else 'clear')


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
os.system('cls' if os.name == 'nt' else 'clear')
p.a.AtributosRandom = a


print("\n--- Seus atributos finais ---")
p.mostrar()
print("-------------------------------------------------")
for nome, valor in a.AtributosRandom.items():
    desc = a.descricao(nome, valor)
    print(f"{nome.capitalize()}: {valor} → {desc}")
print("-------------------------------------------------")
r.mostrarAtributos()
print("-------------------------------------------------")
c.mostrarClasse()