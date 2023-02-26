from .word import Word


class Noun(Word):
    def __str__(self):
        _str = "=" * 20 + "\n"
        _str += f"Word: {self.word}\n"
        _str += f"Kas?: {self.root}{self.v}\n"
        _str += f"Ko?: {self.root}{self.k}\n"
        _str += f"Kam?: {self.root}{self.n}\n"
        _str += f"Ką?: {self.root}{self.g}\n"
        _str += f"Kuo?: {self.root}{self.i}\n"
        _str += f"Kur?: {self.root}{self.vt}\n"
        return _str


class NounMaleSingleAs(Noun):
    v = "as"
    k = "o"
    n = "ui"
    g = "ą"
    i = "u"
    vt = "e"


class NounMaleSingleIs(Noun):
    v = "is"
    k = "io"
    n = "iui"
    g = "į"
    i = "iu"
    vt = "yje"


class NounMaleSingleUs(Noun):
    v = "us"
    k = "aus"
    n = "ui"
    g = "ų"
    i = "umi"
    vt = "uje"


class NounMalePluralAi(Noun):
    v = "ai"
    k = "ų"
    n = "ams"
    g = "us"
    i = "ais"
    vt = "uose"


class NounMalePluralUs(Noun):
    v = "ūs"
    k = "ų"
    n = "ums"
    g = "us"
    i = "umis"
    vt = "uose"


class NounFemaleSingle(Noun):
    def __init__(self, word):
        super().__init__(word)
        self.root = self.word[:-1]


class NounFemaleSingleA(NounFemaleSingle):
    v = "a"
    k = "os"
    n = "ai"
    g = "ą"
    i = "a"
    vt = "oje"


class NounFemaleSingleE(NounFemaleSingle):
    v = "ė"
    k = "ės"
    n = "ei"
    g = "ę"
    i = "e"
    vt = "ėje"


class NounFemalePluralOs(Noun):
    v = "os"
    k = "ų"
    n = "oms"
    g = "as"
    i = "omis"
    vt = "ose"


class NounFemalePluralEs(Noun):
    v = "ės"
    k = "ių"
    n = "ėms"
    g = "es"
    i = "ėmis"
    vt = "ėse"


class NounFactory:
    @staticmethod
    def create_word(word):
        if word.endswith("as"):
            return NounMaleSingleAs(word)
        elif word.endswith("is"):
            return NounMaleSingleIs(word)
        elif word.endswith("us"):
            return NounMaleSingleUs(word)
        elif word.endswith("ai"):
            return NounMalePluralAi(word)
        elif word.endswith("ūs"):
            return NounMalePluralUs(word)
        elif word.endswith("a"):
            return NounFemaleSingleA(word)
        elif word.endswith("ė"):
            return NounFemaleSingleE(word)
        elif word.endswith("os"):
            return NounFemalePluralOs(word)
        elif word.endswith("ės"):
            return NounFemalePluralEs(word)
        else:
            raise Exception(f"{word}: Word type not found")
