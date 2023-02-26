from abc import ABC


class Word(ABC):
    v: str = None
    k: str = None
    n: str = None
    g: str = None
    i: str = None
    vt: str = None

    def __init__(self, word: str):
        self.word = word
        self.root = self.word[:-2]

    def get(self, case: str) -> str:
        return self.root + getattr(self, case)


class WordFromForms:
    def __init__(self, forms: list[str]):
        self.word = forms[0]
        self.v = forms[0]
        self.k = forms[1]
        self.n = forms[2]
        self.g = forms[3]
        self.i = forms[4]
        self.vt = forms[5]

    def __getattr__(self, item) -> str:
        return self.__dict__.get(item, "")

    def get(self, case: str) -> str:
        return getattr(self, case)
