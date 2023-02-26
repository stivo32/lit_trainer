import random

from constants import Case, case_russian
from vocabulary.vocabulary import vocabulary


def collect_phrase(sex, count):
    nouns = list(vocabulary[sex][count]['noun'])
    adjectives = list(vocabulary[sex][count]['adjective'])
    pronouns = list(vocabulary[sex][count]['pronoun'])
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    pronoun = random.choice(pronouns)
    return [pronoun, adjective, noun]


def choose_case():
    return random.choice(list(Case)[1:])


def change_phrase(phrase, case):
    changed_phrase = list(map(lambda word: word.get(case), phrase))
    return " ".join(changed_phrase)


def get_initial_phrase(phrase):
    changed_phrase = list(map(lambda word: word.get('v'), phrase))
    return " ".join(changed_phrase)


def train():
    print('Добро пожаловать в тренажер по склонению словосочетаний на литовском!')
    print('Для выхода из программы введите "exit"')
    print('Поехали!')
    print()
    while True:
        sex = random.choice(['male', 'female'])
        count = random.choice(['single', 'plural'])
        phrase = collect_phrase(sex, count)
        case = choose_case()
        changed_phrase = change_phrase(phrase, case.value)
        print(f'Словосочетание: {get_initial_phrase(phrase)}')
        answer = input(f'Просклоняйте словосочетание в падеже: "{case_russian[case]}":\n')
        if answer == changed_phrase:
            print('Верно!')
        elif answer == 'exit':
            break
        else:
            print(f'Неверно! Правильный ответ: {changed_phrase}')
        print()


if __name__ == '__main__':
    train()