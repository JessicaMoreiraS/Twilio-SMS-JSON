from model import usuario
from connect import inserir, update, deletar
from mensagem import smsDoTwilio
import random

cod = random.randint(100000,999999)
nome = input("Digite seu nome: ")
email = input("Digite seu seu email: ")
telefone = input("Digite seu seu telefone: ")

def main():
    user = usuario(nome, email, telefone, cod, False)
    inserir(user)
    smsDoTwilio(cod, telefone)
    print("Enviamos um SMS para o seu celular")
    codVerifica = int(input("Digite o código de confirmação: "))
    if codVerifica == cod:
        user = usuario(nome, email, telefone, cod, True)
        update(user)
        print("Código correto, conta cadastrada com sucesso")
    else:
        deletar(user)
        print("Código incorreto, conta não cadastrada")
main()