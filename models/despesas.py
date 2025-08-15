

from db.database import get_conn

def adicionar (valor: float, data: str, categoria: str, descricao: str | None = None) -> int:
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO despesas (valor, data, categoria, descricao) VALUES (?, ?, ?, ?)",
            (valor, data, categoria, descricao)
        )
        return cur.lastrowid
    
def listar(filtro_data_ini: str | None = None, filtro_data_fim: str | None = None, categoria: str | None = None):
    sql = "SELECT id, valor, data, categoria, descricao from despesas WHERE 1=1 "
    params = []
    if filtro_data_ini:
        sql += "AND date(data) >= date(?)"
        params.append(filtro_data_ini)
    if filtro_data_fim:
        sql += "AND date(data) <= date(?)"
        params.append(filtro_data_fim)
    if categoria:
        sql += "AND categoria = ?"
        params.append(categoria)
    sql += "ORDER BY date(data) DESC, id DESC"
    with get_conn() as conn:
        return conn.execute(sql, params).fetchall()

def atualizar(id_: int, valor: float | None = None, data: str | None = None,categoria: str | None = None, descricao: str | None = None) -> int:
    campos = []
    params = []

    if valor is not None:
        campos.append('valor = ?'); params.append(valor)
    
    if data is not None:
        campos.append('data = ?'); params.append(data)
    
    if categoria is not None:
        campos.append('categoria = ?'); params.append(categoria)
    
    if descricao is not None:
        campos.append('descricao = ?'); params.append(descricao)

    if not campos:
        return 0
    
    params.append(id_)
    with get_conn() as conn:
        cur = conn.execute(f"UPDATE despesas SET {', '.join(campos)} WHERE id = ?", params)
        return cur.rowcount

def deletar(id_: int) -> int:
    with get_conn() as conn:
        cur = conn.execute('DELETE FROM despesas WHERE id = ?',(id_,))
        return cur.rowcount
    
    