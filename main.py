from unittest.mock import sentinel

from Objetos.Aluno import Aluno
from Objetos.Disciplina import *
from Objetos.Funcionarios import Funcionario
from Objetos.Professor import Professor
from db import *


def main():
    print(Disciplina.selectAll(connectDb()))
    dis1 = Disciplina("DESENVOLVIMENTO RÁPIDO DE APLICAÇÕES EM PYTHON","ARA0095", 2025, 3)
    dis2 = Disciplina("ÁLGEBRA LINEAR", "ARA2566", 2025, 3)
    dis1.insert()
    #Aluno("").insert()

    func1 = Funcionario("Rogerio", "rpf1105@gmail.com", "12345678")
    func1.insert()
    prof1 = Professor("rpf1105@gmail.com", "ARA095")
    prof1.insert()
    print(func1.senha)
    senha = func1.senha
    print(senha)


    #print(dis1.select(con))
    #alun1 = Aluno("Rogerio")
    #alun1.insert(con)
    #print(vars(dis2))
if __name__ =="__main__":
    main()