from enum import Enum


class Case(Enum):
    v = 'v'
    k = 'k'
    n = 'n'
    g = 'g'
    i = 'i'
    vt = 'vt'


case_russian = {
    Case.v: 'Именительный',
    Case.k: 'Родительный',
    Case.n: 'Дательный',
    Case.g: 'Винительный',
    Case.i: 'Творительный',
    Case.vt: 'Местный'
}


question = {
    Case.v: 'Kas?',
    Case.k: 'Ko?',
    Case.n: 'Kam?',
    Case.g: 'Ką?',
    Case.i: 'Kuo?',
    Case.vt: 'Kur?'
}
