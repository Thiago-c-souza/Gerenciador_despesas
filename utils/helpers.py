from datetime import datetime

def is_date_iso(s: str) -> str | None:
    s = s.strip()
    if not s:
        return None
    formatos = [
        "%Y-%m-%d",  # 2025-08-14
        "%d-%m-%Y",  # 14-08-2025
        "%Y/%m/%d",  # 2025/08/14
        "%d/%m/%Y",  # 14/08/2025
        "%Y%m%d",    # 20250814
        "%d%m%Y",    # 14082025
    ]
    for fmt in formatos:
        try:
            dt = datetime.strptime(s, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None
    

def ask(prompt:str, required: bool = True) -> str:
    while True:
        v = input(prompt).strip()
        if not v and required:
            print("Campo obrigatorio.")
            continue
        return v

def ask_date(prompt: str, allow_empty: bool = False) -> str | None:
    while True:
        v = input(prompt).strip()
        if not v and allow_empty:
            return None
        iso = is_date_iso(v)
        if iso:
            return iso
        print(' Data invalida.')

def fmt_real(v: float) -> str:
    s = f"{v:,.2f}"
    return "R$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")