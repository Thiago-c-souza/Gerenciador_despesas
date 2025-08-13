from db.database import init_db as db
from models import desepesas
from utils.helpers import ask, ask_date

def menu():
    print("\n=== Gerenciador de Despesas ===")
    print("1) Adicionar")
    print("2) Lista")
    print("3) Atualizar")
    print("4) Deletar")
    print("0) Sair")

def acao_adicionar():
    pass

if __name__ == '__main__':
    db()
    print("Banco iniciado com sucesso!")