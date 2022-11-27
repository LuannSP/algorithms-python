"""
CPF: 168.995.350-09
------------------------------------------------------
1 * 10  = 10            #   1 * 11  = 11 <-
6 * 9   = 54            #   6 * 10  = 60
8 * 8   = 64            #   8 * 9   = 72
9 * 7   = 63            #   9 * 8   = 72
9 * 6   = 54            #   9 * 7   = 63
5 * 5   = 25            #   5 * 6   = 30
3 * 4   = 12            #   3 * 5   = 15
5 * 3   = 15            #   5 * 4   = 20
0 * 2   = 0             #   0 * 3   = 0
                        #-> 0 * 2   = 0
         297            #             343
11 - (297 % 11) = 11    #   11 - (343 % 11) = 9
11 > 9 = 0              #
Digito 1 = 0            # Digito 2 = 9
"""
from random import randint


def generateCpf() -> str:
    cpf = str(randint(100000000, 999999999))
    newCpf = _returnCpf(cpf)
    return newCpf


def validateCpf(cpf: str) -> bool:
    if type(cpf) != str:
        raise TypeError('this is not string')

    if not cpf.isnumeric():
        raise TypeError('only numbers')

    if cpf == cpf[0] * 11:
        raise ValueError('numerical sequences are not allowed')

    if len(cpf) > 11:
        cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11:
        raise ValueError('there are not 11 numbers in the cpf')

    newCpf = cpf[:-2]

    if cpf == _returnCpf(newCpf):
        return True
    return False


def _returnCpf(newCpf: str) -> str:
    digit = 0
    for i, c in enumerate(newCpf[::-1], 2):
        digit += i*int(c)
    else:
        digit = 11 - (digit % 11)
        result = 0 if digit > 9 else digit
        newCpf += str(result)
        if len(newCpf) == 11:
            return newCpf
        return _returnCpf(newCpf)
