from datetime import datetime

def is_date_iso(s: str) -> bool:
    try:
        datetime.strftime(s, "%Y-%m-%d")
        return True
    except Exception:
        return False

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
        if is_date_iso(v):
            return v
        print("Use o formato YYYY-MM-DD.")