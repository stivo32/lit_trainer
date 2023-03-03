from .word import Word


class AdjectiveMale(Word):
    def __str__(self):
        _str = "=" * 20 + "\n"
        _str += f"Word: {self.word}\n"
        _str += f"Koks?: {self.root}{self.v}\n"
        _str += f"Kokio?: {self.root}{self.k}\n"
        _str += f"kokiam?: {self.root}{self.n}\n"
        _str += f"Kokį?: {self.root}{self.g}\n"
        _str += f"kokiu?: {self.root}{self.i}\n"
        _str += f"kokiame?: {self.root}{self.vt}\n"
        return _str


class AdjectiveFemale(Word):
    def __str__(self):
        _str = "=" * 20 + "\n"
        _str += f"Word: {self.word}\n"
        _str += f"Kokia?: {self.root}{self.v}\n"
        _str += f"Kokios?: {self.root}{self.k}\n"
        _str += f"kokiai?: {self.root}{self.n}\n"
        _str += f"Kokią?: {self.root}{self.g}\n"
        _str += f"kokia?: {self.root}{self.i}\n"
        _str += f"kokioje?: {self.root}{self.vt}\n"
        return _str


class AdjectiveMaleSingleAs(AdjectiveMale):
    v = "as"
    k = "o"
    n = "am"
    g = "ą"
    i = "u"
    vt = "ame"


class AdjectiveMaleSingleUs(AdjectiveMale):
    v = "us"
    k = "aus"
    n = "iam"
    g = "ų"
    i = "iu"
    vt = "iame"


class AdjectiveMaleSingleIs(AdjectiveMale):
    v = "is"
    k = "io"
    n = "iam"
    g = "į"
    i = "iu"
    vt = "iame"


class AdjectiveMalePluralI(AdjectiveMale):
    v = "i"
    k = "ių"
    n = "iems"
    g = "ius"
    i = "iais"
    vt = "iuose"

    def __init__(self, word):
        super().__init__(word)
        self.root = self.word[:-1]


class AdjectiveMalePluralUs(AdjectiveMale):
    v = "ūs"
    k = "ių"
    n = "iems"
    g = "ius"
    i = "iais"
    vt = "iuose"


class AdjectiveMalePluralAi(AdjectiveMale):
    v = "ai"
    k = "ų"
    n = "ams"
    g = "us"
    i = "ais"
    vt = "uose"


class AdjectiveFemaleSingleA(AdjectiveFemale):
    v = "a"
    k = "os"
    n = "ai"
    g = "ą"
    i = "a"
    vt = "oje"

    def __init__(self, word):
        super().__init__(word)
        self.root = self.word[:-1]


class AdjectiveFemaleSingleI(AdjectiveFemale):
    v = "i"
    k = "ios"
    n = "iai"
    g = "ią"
    i = "ia"
    vt = "ioje"

    def __init__(self, word):
        super().__init__(word)
        self.root = self.word[:-1]


class AdjectiveFemaleSingleE(AdjectiveFemale):
    v = "e"
    k = "ės"
    n = "ei"
    g = "ę"
    i = "e"
    vt = "ėje"

    def __init__(self, word):
        super().__init__(word)
        self.root = self.word[:-1]


class AdjectiveFemalePluralOs(AdjectiveFemale):
    v = "os"
    k = "ų"
    n = "oms"
    g = "as"
    i = "omis"
    vt = "ose"


class AdjectiveFemalePluralEs(AdjectiveFemale):
    v = "ės"
    k = "ių"
    n = "ėms"
    g = "es"
    i = "ėmis"
    vt = "ėse"


class AdjectiveFactory:
    @staticmethod
    def create_word(word, sex):
        if sex == "male":
            if word.endswith("as"):
                return AdjectiveMaleSingleAs(word)
            elif word.endswith("us"):
                return AdjectiveMaleSingleUs(word)
            elif word.endswith("is"):
                return AdjectiveMaleSingleIs(word)
            elif word.endswith("i"):
                return AdjectiveMalePluralI(word)
            elif word.endswith("ūs"):
                return AdjectiveMalePluralUs(word)
            elif word.endswith("ai"):
                return AdjectiveMalePluralAi(word)
            else:
                raise Exception("Unknown word type")
        else:
            if word.endswith("a"):
                return AdjectiveFemaleSingleA(word)
            elif word.endswith("i"):
                return AdjectiveFemaleSingleI(word)
            elif word.endswith("e"):
                return AdjectiveFemaleSingleE(word)
            elif word.endswith("os"):
                return AdjectiveFemalePluralOs(word)
            elif word.endswith("ės"):
                return AdjectiveFemalePluralEs(word)
            else:
                raise Exception("Unknown word type")
