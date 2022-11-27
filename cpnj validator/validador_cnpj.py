import re

REGRESSIVE = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def check_cnpj(cnpj: str) -> bool:
    cnpj = clear_cnpj(cnpj)
    try:
        if not check_sequence(cnpj):
            return False
        new_cnpj = cacl(cnpj, digit=1)
        new_cnpj = cacl(new_cnpj, digit=2)
    except Exception as e:
        return False
    if new_cnpj == cnpj:
        return True
    return False


def cacl(cnpj: str, digit: str) -> str:
    if digit == 1:
        new_regressivos = REGRESSIVE[1::]
        new_cnpj = cnpj[:-2]
    elif digit == 2:
        new_regressivos = REGRESSIVE
        new_cnpj = cnpj
    total = 0
    for i, r in enumerate(new_regressivos):
        total += int(cnpj[i]) * r
    d = 11 - (total % 11)
    d = d if d <= 9 else 0
    return f'{new_cnpj}{d}'


def check_sequence(cnpj: str) -> bool:
    s = cnpj[0] * len(cnpj)
    if s == cnpj:
        return False
    return True


def clear_cnpj(cnpj: str) -> str:
    return re.sub(r'[^0-9]', '', cnpj)
