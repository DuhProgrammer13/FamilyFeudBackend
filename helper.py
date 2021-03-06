import database_models
from random import choice


def get_random_survey(_min, _max, _search):
    r_dict = {}
    database_models.Survey.title.like("%" + str(_search) + "%")
    database_models.Survey.query.filter(database_models.Survey.answer_count >= int(_min))
    surveys = database_models.Survey.query.filter(database_models.Survey.title.like("%" + str(_search) + "%"))\
        .filter(database_models.Survey.answer_count >= int(_min))\
        .filter(database_models.Survey.answer_count <= int(_max)).all()
    survey = choice(surveys)
    answers = database_models.Answer.query.filter_by(survey=survey.id).all()

    r_dict["title"] = survey.title
    r_dict["id"] = survey.id
    r_dict["answers"] = [
        {"answer": answer.answer, "value": answer.value} for answer in answers
        ]
    return r_dict


def get_surveys(_min, _max, _search, start, count):
    r_dict = {}

    surveys = database_models.Survey.query.filter(database_models.Survey.title.like("%" + str(_search) + "%"))\
        .filter(database_models.Survey.answer_count >= int(_min))\
        .filter(database_models.Survey.answer_count <= int(_max))\
        .all()

    surveys = surveys[start:start+count]
    r_dict["surveys"] = [
        {"title": survey.title, "id": survey.id} for survey in surveys
        ]
    return r_dict


def get_answers_json(game):
    return [{"answer": answer.answer, "id": answer.id, "value": answer.value, "answered": answer.answered}
            for answer in game.survey.answers]
