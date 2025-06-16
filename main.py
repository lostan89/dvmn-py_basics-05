import os
import file_operations
import random
from faker import Faker


def main():

    os.makedirs('output', exist_ok=True)

    for number in range(10):

        skills = [
            'Стремительный прыжок',
            'Электрический выстрел',
            'Ледяной удар',
            'Стремительный удар',
            'Кислотный взгляд',
            'Тайный побег',
            'Ледяной выстрел',
            'Огненный заряд'
        ]

        runic = {
            "а": "а͠",
            "б": "б̋",
            "в": "в͒͠",
            "г": "г͒͠",
            "д": "д̋",
            "е": "е͠",
            "ё": "ё͒͠",
            "ж": "ж͒",
            "з": "з̋̋͠",
            "и": "и",
            "й": "й͒͠",
            "к": "к̋̋",
            "л": "л̋͠",
            "м": "м͒͠",
            "н": "н͒",
            "о": "о̋",
            "п": "п̋͠",
            "р": "р̋͠",
            "с": "с͒",
            "т": "т͒",
            "у": "у͒͠",
            "ф": "ф̋̋͠",
            "х": "х͒͠",
            "ц": "ц̋",
            "ч": "ч̋͠",
            "ш": "ш͒͠",
            "щ": "щ̋",
            "ъ": "ъ̋͠",
            "ы": "ы̋͠",
            "ь": "ь̋",
            "э": "э͒͠͠",
            "ю": "ю̋͠",
            "я": "я̋",
            "А": "А͠",
            "Б": "Б̋",
            "В": "В͒͠",
            "Г": "Г͒͠",
            "Д": "Д̋",
            "Е": "Е",
            "Ё": "Ё͒͠",
            "Ж": "Ж͒",
            "З": "З̋̋͠",
            "И": "И",
            "Й": "Й͒͠",
            "К": "К̋̋",
            "Л": "Л̋͠",
            "М": "М͒͠",
            "Н": "Н͒",
            "О": "О̋",
            "П": "П̋͠",
            "Р": "Р̋͠",
            "С": "С͒",
            "Т": "Т͒",
            "У": "У͒͠",
            "Ф": "Ф̋̋͠",
            "Х": "Х͒͠",
            "Ц": "Ц̋",
            "Ч": "Ч̋͠",
            "Ш": "Ш͒͠",
            "Щ": "Щ̋",
            "Ъ": "Ъ̋͠",
            "Ы": "Ы̋͠",
            "Ь": "Ь̋",
            "Э": "Э͒͠͠",
            "Ю": "Ю̋͠",
            "Я": "Я̋",
            " ": " ",
        }

        skill_runic_1 = ''

        runic_skills = []

        for skill in skills:
            skill_runic_1 = ''
            for letter in skill:
                skill_runic_1 = skill_runic_1 + runic[letter]
            runic_skills.append(skill_runic_1)

        unique_skills = random.sample(runic_skills, 3)

        skill_1, skill_2, skill_3 = unique_skills

        context = {
            'first_name': Faker('ru_RU').first_name(),
            'last_name': Faker('ru_RU').last_name(),
            'job': Faker('ru_RU').job(),
            'town': Faker('ru_RU').city(),
            'strength': random.randint(3, 18),
            'agility': random.randint(3, 18),
            'endurance': random.randint(3, 18),
            'intelligence': random.randint(3, 18),
            'luck': random.randint(3, 18),
            'skill_1': skill_1,
            'skill_2': skill_2,
            'skill_3': skill_3
        }

        file_operations.render_template(
            "template.svg", 'output/result-{}.svg'.format(number), context
        )


if __name__ == '__main__':
    main()
