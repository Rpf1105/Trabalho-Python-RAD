from db import *


def main():
    dis1 = Disciplina("DESENVOLVIMENTO RÁPIDO DE APLICAÇÕES EM PYTHON","ARA0095", 2025, 3)
    dis2 = Disciplina("PROGRAMAÇÃO ORIENTADA A OBJETOS EM JAVA", "TMS0995", 2025, 3)
    con = connectDbAluno()

    rows = Disciplina.selectAll(con)
    print(rows)

    alun1 = Aluno("Rogerio")
    alun1.insert(con)
if __name__ =="__main__":
    main()