from connect import excluirdados, inserir, mostrardados
from model import Pessoa


def main():
    p = Pessoa('miqueias',12,12)
    excluirdados(p.nome)
main()