import random

from colorama import Fore, Style, init

from .constants import Case, case_russian, question
from .vocabulary.vocabulary import vocabulary

init()


def collect_phrase():
    sex = random.choice(['male', 'female'])
    count = random.choice(['single', 'plural'])
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
    return changed_phrase


def get_initial_phrase(phrase):
    changed_phrase = list(map(lambda word: word.get('v'), phrase))
    return changed_phrase


def wrap_in_color(phrase, color):
    return f'{color}{phrase}{Style.RESET_ALL}'


def joined(phrase):
    return " ".join(phrase)


def print_rules(words):
    print(f'Таблица склонений для слов с ошибками:')
    messages = []
    for case in list(Case):
        case_message = f'| {question[case]:4} |'
        for word in words:
            max_len = max([len(word.get(case.value)) for case in list(Case)])
            case_message += f' {word.get(case.value).ljust(max_len, " ")} |'
        messages.append(case_message)
    max_len = max([len(message) for message in messages])
    print('=' * max_len)
    for message in messages:
        print(message)
    print('=' * max_len)


def train():
    print('Добро пожаловать в тренажер по склонению словосочетаний на литовском!')
    print('Для выхода из программы введите "exit"')
    print('Поехали!')
    print()
    while True:
        phrase = collect_phrase()
        case = choose_case()
        changed_phrase = change_phrase(phrase, case.value)
        print(f'Словосочетание: {joined(get_initial_phrase(phrase))}')
        printed_case = wrap_in_color(f"{case_russian[case]}({question[case]})", Fore.RED)
        answer = input(f'Просклоняйте словосочетание в падеже: "{printed_case}":\n')
        answer = answer.lower()
        if answer == joined(changed_phrase):
            print('Верно!')
        elif answer == 'exit':
            break
        else:
            splited_answer = answer.split()
            if len(splited_answer) != len(changed_phrase):
                print(f'Неверно! Правильный ответ: {joined(changed_phrase)}\n')
            else:
                errors_indexes = [splited_answer[i] != changed_phrase[i] for i in range(len(splited_answer))]
                output_phrase = [
                    word if not errors_indexes[i] else wrap_in_color(word, Fore.YELLOW)
                    for i, word in enumerate(changed_phrase)
                ]
                print(f'Неверно! Правильный ответ: {joined(output_phrase)}')
                print_rules([phrase[i] for i, has_error in enumerate(errors_indexes) if has_error])
        print()


if __name__ == '__main__':
    train()
