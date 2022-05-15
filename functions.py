
import json

# DATA_PATH = candidates.json

def load_candidates():
    """ Функция загружает данные о кандидатах"""

    with open('candidates.json', encoding='utf-8') as f:
        file = f.read()
        data_file = json.loads(file)

    return data_file

def get_all_candidates():
    """ Функция получает список всех кандидатов"""
    list_of_candidates = load_candidates()
    return list_of_candidates



def get_id_cand(id):
    """ Функция получает кандидата по id"""
    list_of_candidates = load_candidates()
    for candidate in list_of_candidates:
        if candidate["id"] == id:
            return candidate


def get_skills_of_cand(skill_name):
    """ Функция получает навыки кандидата"""
    skilled_candidates = []
    skill_name = skill_name.lower()

    list_of_candidates = load_candidates()
    for candidate in list_of_candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            skilled_candidates.append(candidate)
            continue

    return skilled_candidates

print(get_skills_of_cand('go'))