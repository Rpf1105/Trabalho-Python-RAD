from unittest.mock import sentinel

from db import *


def main():
    dis1 = Disciplina("DESENVOLVIMENTO RÁPIDO DE APLICAÇÕES EM PYTHON","ARA0095", 2025, 3)
    dis2 = Disciplina("ÁLGEBRA LINEAR", "ARA2566", 2025, 3)
    dis1.insert(connectDb())
    Aluno("Rogerio").insert(connectDb())

    func1 = Funcionario("Rogerio", "rpf1105", "12345678", "Admin")
    func1.insert(connectDb())
    print(func1.chave)
    senhaenc = func1.senha
    key = Fernet(func1.chave)
    senha = key.decrypt(senhaenc).decode()
    print(senha)
    print(senhaenc)


    #print(dis1.select(con))
    #alun1 = Aluno("Rogerio")
    #alun1.insert(con)
    #print(vars(dis2))
if __name__ =="__main__":
    main()