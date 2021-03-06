import database_models


SETUP = -1
SINGLE = 0
DOUBLE = 1
TRIPLE = 2
SUDDEN_DEATH = 3
FAST_MONEY = 4


class Family:
    def __init__(self, name):
        self.name = name
        self.points = 0


class Answer:
    _id = 0

    def __init__(self, answer, value):
        self.id = Answer._id
        self.answered = False
        self.answer = answer
        self.value = value
        Answer._id += 1


class Survey:
    def __init__(self, answers, survey):
        self.answers = answers
        self.survey = survey


class Game:
    def __init__(self, survey_id):
        Answer._id = 0
        self.survey = get_survey(survey_id)
        self.points = 0

    def reveal(self, answer_id):
        for answer in self.survey.answers:
            if answer.id == answer_id:
                if not answer.answered:
                    self.points += answer.value
                answer.answered = True

    def set_survey(self, survey_id):
        self.survey = get_survey(survey_id)
        self.points = 0

    def answer(self, answer_num):
        self.survey.answers[answer_num].answered = True


def get_survey(survey_id):
    _survey = database_models.Survey.query.filter_by(id=survey_id).first()
    return Survey(get_answers(survey_id), _survey.title)


def get_answers(survey_id):
    _answers = database_models.Answer.query.filter_by(survey=survey_id)
    r_answers = []
    for answer in _answers:
        r_answers.append(Answer(answer.answer, answer.value))
    return r_answers
