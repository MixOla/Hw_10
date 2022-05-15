def build_html_for_one_candidate(candidate):
    """Формирует html код для вывода одного кандидата"""
    code_for_candidate = ""

    code_for_candidate += f'<img src>=\"{candidate["picture"]}\">\n'
    code_for_candidate += f'Имя кандидата - {candidate["name"]}\n'
    code_for_candidate += f'Позиция кандидата - {candidate["position"]}\n'
    code_for_candidate += f'Навыки - {candidate["skills"]}\n'
    code_for_candidate += "\n"

    return "<pre>" + code_for_candidate + "</pre>"


def build_html_for_all_candidates(candidates):
    """Формирует html код для вывода всех кандидатов"""
    code_for_candidate = ""

    for candidate in candidates:
        code_for_candidate += f'Имя кандидата - {candidate["name"]}\n'
        code_for_candidate += f'Позиция кандидата - {candidate["position"]}\n'
        code_for_candidate += f'Навыки - {candidate["skills"]}\n'

        code_for_candidate += "\n"

    return "<pre>" + code_for_candidate + "</pre>"