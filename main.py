from db.database import init_db as db
from models import despesas
from utils.helpers import ask, ask_date

def menu():
    print("\n=== Gerenciador de Despesas ===")
    print("1) Adicionar")
    print("2) Lista")
    print("3) Atualizar")
    print("4) Deletar")
    print("0) Sair")

def acao_adicionar():
    try:
        valor = float(ask("valor (ex: 123.45)"))
        data = ask_date("data (YYYY-MM-DD)")
        categoria = ask("categoria: ")
        descricao = ask("descrição (pode vazio)", required=False)
        new_id = despesas.adicionar(valor, data, categoria, descricao or None)
        print(f"Despesa adiciona (id={new_id}).")
    except ValueError:
        print("Valor invalido")

def acao_listar():
    ini = ask_date("Filtrar Data inicial (YYYY-MM-DD) [Enter p/pular]: ", allow_empty=True)
    fim = ask_date("Filtrar Data final (YYYY-MM-DD) [Enter p/pular]: ", allow_empty=True)
    cat = ask("Filtrar categoria [Enter p/pular]:", required=False) or None
    rows = despesas.listar(ini, fim, cat)
    if not rows:
        print("Nenhum registro.")
        return
    print("\nID | DATA     |VALOR     CATEGORIA     |DESCRIÇÃO")
    print("-" * 60)
    for r in rows:
        _id, valor, data, categoria, descricao = r
        print(f"{_id:>2} | {data:<10} | {valor:>8.2f} | {categoria:<9} | {descricao or ''}")

def acao_atualizar():
    try:
        _id = int(ask("ID da despesa: "))
    except ValueError:
        print("ID inválido.")
        return
    val = ask("Novo valor [Enter p/ manter]: ", required=False)
    valor = float(val) if val else None
    data = ask_date("Nova data (YYYY-MM-DD) [Enter p/ manter]: ", allow_empty=True)
    categoria = ask("Nova categoria [Enter p/ manter]: ", required=False) or None
    descricao = ask("Nova descrição [Enter p/ manter]: ", required=False)
    if descricao == "":
        descricao = None  # manter
    linhas = despesas.atualizar(_id, valor, data, categoria, descricao)
    print("✔ Atualizado." if linhas else "Nada atualizado. Verifique o ID.")

def acao_deletar():
    try:
        _id = int(ask("ID da despesa: "))
    except ValueError:
        print("ID inválido.")
        return
    conf = ask(f"Confirma deletar id={_id}? (s/N): ", required=False).lower()
    if conf == "s":
        linhas = despesas.deletar(_id)
        print("✔ Deletado." if linhas else "ID não encontrado.")
    else:
        print("Cancelado.")

if __name__ == "__main__":
    db()
    while True:
        menu()
        op = ask("Escolha: ", required=False)
        if op == "1":
            acao_adicionar()
        elif op == "2":
            acao_listar()
        elif op == "3":
            acao_atualizar()
        elif op == "4":
            acao_deletar()
        elif op == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


