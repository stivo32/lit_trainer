import os

from dotenv import load_dotenv

from schemes.adjective import AdjectiveFactory
from schemes.noun import NounFactory
from schemes.word import WordFromForms

load_dotenv('../extra_vocabulary.env')

# nouns

male_single_nouns = ['vietas', 'namas', 'vilnius', 'minskas', 'butas']
male_plural_nouns = ['tevai', 'namai', 'sunūs']
female_single_nouns = ['kavinė', 'nuolaida', 'draugė', 'mama']
female_plural_nouns = ['kavinės', 'nuolaidos', 'draugės', 'mamos']

# adjectives


male_single_adjectives = ['šviesus', 'geltonas', 'geras', 'didelis', 'gražus', 'skanus']
male_plural_adjectives = ['šviesūs', 'geltoni', 'geri', 'dideli', 'gražūs', 'skani']
female_single_adjectives = ['gera', 'graži', 'skani', 'šviesi', 'geltona']
female_plural_adjectives = ['geros', 'gražios', 'skanios', 'šviesios', 'geltonos']

# pronouns

common_single_noun_pronouns = [
    ['aš', 'manęs', 'man', 'mane', 'manimi', 'manyje'],
    ['tu', 'tave', 'tavęs', 'tave', 'tavimi', 'tavyje'],
]
common_plural_noun_pronouns = [
    ['mes', 'mūsų', 'mums', 'mus', 'mumis', 'mumyse'],
    ['jūs', 'jūsų', 'jums', 'jus', 'jumis', 'jumyse'],
]
male_single_noun_pronouns = [['jis', 'jo', 'jam', 'jį', 'juo', 'jame'], *common_single_noun_pronouns]
male_plural_noun_pronouns = [['jie', 'ju', 'jų', 'jų', 'jais', 'jose'], *common_plural_noun_pronouns]
female_single_noun_pronouns = [['ji', 'jos', 'jos', 'ją', 'ja', 'joje'], *common_single_noun_pronouns]
female_plural_noun_pronouns = [['jos', 'jos', 'jų', 'jų', 'jomis', 'jose'], *common_plural_noun_pronouns]

male_single_adjective_pronouns = [
    ['kitas', 'kito', 'kitam', 'kitą', 'kitu', 'kitame'],
    ['visas', 'viso', 'visam', 'visą', 'visu', 'visame'],
    ['kuris', 'kurio', 'kuriam', 'kurį', 'kuriuo', 'kuriame'],
    ['šis', 'šio', 'šiam', 'šį', 'šiuo', 'šiame'],
    ['tas', 'to', 'tam', 'tą', 'tu', 'tame'],
    ['anas', 'ano', 'anam', 'aną', 'anu', 'aname'],
]
male_plural_adjective_pronouns = [
    ['kiti', 'kitų', 'kitiems', 'kitus', 'kitais', 'kituose'],
    ['visi', 'visų', 'visiems', 'visus', 'visais', 'visuose'],
    ['kurie', 'kurių', 'kuriems', 'kuriuos', 'kuriais', 'kuriuose'],
    ['šie', 'šių', 'šiems', 'šiuos', 'šiais', 'šiuose'],
    ['tie', 'tų', 'tiems', 'tuos', 'tais', 'tuose'],
    ['anie', 'anų', 'aniems', 'anuos', 'anais', 'anuose'],
]
female_single_adjective_pronoun = [
    ['kita', 'kitos', 'kitai', 'kitą', 'kita', 'kitoje'],
    ['visa', 'visos', 'visai', 'visą', 'visa', 'visoje'],
    ['kuri', 'kurios', 'kuriai', 'kurią', 'kuria', 'kurioje'],
    ['ši', 'šios', 'šiai', 'šią', 'šia', 'šioje'],
    ['ta', 'tos', 'tai', 'tą', 'ta', 'toje'],
    ['ana', 'anos', 'anai', 'aną', 'ana', 'anoje'],
]
female_plural_adjective_pronouns = [
    ['kitos', 'kitų', 'kitoms', 'kitas', 'kitomis', 'kitose'],
    ['visos', 'visų', 'visoms', 'visas', 'visomis', 'visose'],
    ['kurios', 'kurių', 'kurioms', 'kurias', 'kuriomis', 'kuriuose'],
    ['šios', 'šių', 'šioms', 'šias', 'šiomis', 'šiose'],
    ['tos', 'tų', 'toms', 'tas', 'tomis', 'tose'],
    ['anos', 'anų', 'anoms', 'anas', 'anomis', 'anose'],
]

vocabulary = {
    'male': {
        'single': {'adjective': set(), 'noun': set(), 'pronoun': set()},
        'plural': {'adjective': set(), 'noun': set(), 'pronoun': set()},
    },
    'female': {
        'single': {'adjective': set(), 'noun': set(), 'pronoun': set()},
        'plural': {'adjective': set(), 'noun': set(), 'pronoun': set()},
    },
}


def add_words_from_env():
    user_male_single_nouns_raw = os.getenv('MALE_SINGLE_NOUN', '')
    user_male_single_nouns = user_male_single_nouns_raw.split(' ') if user_male_single_nouns_raw else []
    user_male_plural_nouns_raw = os.getenv('MALE_PLURAL_NOUN', '')
    user_male_plural_nouns = user_male_plural_nouns_raw.split(' ') if user_male_plural_nouns_raw else []
    user_female_single_nouns_raw = os.getenv('FEMALE_SINGLE_NOUN', '')
    user_female_single_nouns = user_female_single_nouns_raw.split(' ') if user_female_single_nouns_raw else []
    user_female_plural_nouns_raw = os.getenv('FEMALE_PLURAL_NOUN', '')
    user_female_plural_nouns = user_female_plural_nouns_raw.split(' ') if user_female_plural_nouns_raw else []

    male_single_nouns.extend(user_male_single_nouns)
    male_plural_nouns.extend(user_male_plural_nouns)
    female_single_nouns.extend(user_female_single_nouns)
    female_single_nouns.extend(user_female_plural_nouns)

    user_male_single_adjectives_raw = os.getenv('MALE_SINGLE_ADJECTIVE', '')
    user_male_single_adjectives = user_male_single_adjectives_raw.split(' ') if user_male_single_adjectives_raw else []
    user_male_plural_adjectives_raw = os.getenv('MALE_PLURAL_ADJECTIVE', '')
    user_male_plural_adjectives = user_male_plural_adjectives_raw.split(' ') if user_male_plural_adjectives_raw else []
    user_female_single_adjectives_raw = os.getenv('FEMALE_SINGLE_ADJECTIVE', '')
    user_female_single_adjectives = (
        user_female_single_adjectives_raw.split(' ') if user_female_single_adjectives_raw else []
    )
    user_female_plural_adjectives_raw = os.getenv('FEMALE_PLURAL_ADJECTIVE', '')
    user_female_plural_adjectives = (
        user_female_plural_adjectives_raw.split(' ') if user_female_plural_adjectives_raw else []
    )

    male_single_adjectives.extend(user_male_single_adjectives)
    male_plural_adjectives.extend(user_male_plural_adjectives)
    female_single_adjectives.extend(user_female_single_adjectives)
    female_plural_adjectives.extend(user_female_plural_adjectives)


def fill_vocabulary():
    vocabulary['male']['single']['noun'] = {
        *[
            NounFactory.create_word(
                word,
            )
            for word in male_single_nouns
        ],
        *[WordFromForms(forms) for forms in male_single_noun_pronouns],
    }
    vocabulary['male']['plural']['noun'] = {
        *[NounFactory.create_word(word) for word in male_plural_nouns],
        *[WordFromForms(forms) for forms in male_plural_noun_pronouns],
    }
    vocabulary['female']['single']['noun'] = {
        *[NounFactory.create_word(word) for word in female_single_nouns],
        *[WordFromForms(forms) for forms in female_single_noun_pronouns],
    }
    vocabulary['female']['plural']['noun'] = {
        *[NounFactory.create_word(word) for word in female_plural_nouns],
        *[WordFromForms(forms) for forms in female_plural_noun_pronouns],
    }
    vocabulary['male']['single']['adjective'] = {
        AdjectiveFactory.create_word(word, 'male') for word in male_single_adjectives
    }
    vocabulary['male']['plural']['adjective'] = {
        AdjectiveFactory.create_word(word, 'male') for word in male_plural_adjectives
    }
    vocabulary['female']['single']['adjective'] = {
        AdjectiveFactory.create_word(word, 'female') for word in female_single_adjectives
    }
    vocabulary['female']['plural']['adjective'] = {
        AdjectiveFactory.create_word(word, 'female') for word in female_plural_adjectives
    }
    vocabulary['male']['single']['pronoun'] = {WordFromForms(forms) for forms in male_single_adjective_pronouns}
    vocabulary['male']['plural']['pronoun'] = {WordFromForms(forms) for forms in male_plural_adjective_pronouns}
    vocabulary['female']['single']['pronoun'] = {WordFromForms(forms) for forms in female_single_adjective_pronoun}
    vocabulary['female']['plural']['pronoun'] = {WordFromForms(forms) for forms in female_plural_adjective_pronouns}


add_words_from_env()
fill_vocabulary()
