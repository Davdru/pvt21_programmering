import requests

from quiz2.data_model import Question, Answer
import json


class BaseAPI:
    def get_questions(self) -> list[Question]:
        raise NotImplementedError

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError


class QuizAPI(BaseAPI):
    __url: str #  ett understreck _ indikerar att detta är något vi inte skall pilla på
    # två understreck, som i det här fallet __url gör så python skriver om namnet på attributet/variabeln så att
    # det blir betydligt svårare att komma åt

    def __init__(self, url):
        self.__url = url

    def get_questions(self) -> list[Question]:
        questions = requests.get(self.__url).json()['questions']
        return self._parse_questions(questions)

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError

    def _parse_questions(self, questions):
        return [self._parse_question(q) for q in questions]

    def _parse_answer(self, a) -> Answer:
        return Answer(a['answer'], a['correct'])

    def _parse_answers(self, answers) -> list[Answer]:
        return [self._parse_answer(a) for a in answers]

    def _parse_question(self, q) -> Question:
        return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], self._parse_answers(q['answers']))


class FileAPI(QuizAPI):
    def __init__(self):
        pass

    def get_questions(self) -> list[Question]:
        with open("questions.json") as f:
            return self._parse_questions(json.load(f)['questions'])



class DummyAPI(BaseAPI):
    def __init__(self):
        pass

    def get_questions(self) -> list[Question]:
        return [Question(1, "Vad är meningen med universum livet och allting", 10, 5, [Answer("42", True), Answer("Det finns ingen", False)])]

    def post_answer(self, question:Question, correct: bool):
        raise NotImplementedError

