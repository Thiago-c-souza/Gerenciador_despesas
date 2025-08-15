from db.database import get_conn

def filtro_perildo(filtro_data_ini: str | None, filtro_data_fim: str | None):
    where = "WHERE 1=1 "
    params = []
    if filtro_data_ini:
        where += "AND date(data) >= date(?) "
        params.append(filtro_data_ini)
    if filtro_data_fim:
        where += "AND date(data) <= date(?) "
        params.append(filtro_data_fim)
    return where, params

def total_categoria(filtro_data_ini: str | None, filtro_data_fim: str | None):
    where, params = filtro_perildo(filtro_data_ini, filtro_data_fim)
    sql = f"""
        SELECT  categoria, SUM(valor) AS total
        FROM despesas
        {where}
        GROUP BY categoria
        ORDER BY total DESC, categoria ASC
"""
    with get_conn() as conn:
        return conn.execute(sql, params).fetchall()

def total_mes(filtro_data_ini: str | None, filtro_data_fim: str | None):
    where, params = filtro_perildo(filtro_data_ini, filtro_data_fim)
    sql = f"""
        SELECT strftime('%Y-%m', date(data)) AS mes, SUM(valor) AS total
        FROM despesas
        {where}
        GROUP BY mes
        ORDER BY mes DESC
"""
    with get_conn() as conn:
        return conn.execute(sql, params).fetchall()