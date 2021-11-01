import requests

from quiz2.data_model import Answer, Question

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


def get_questions() -> list[Question]:
    response = requests.get(QUIZ_URL).json()
    res = []
    for q in response['questions']:
        # Här skall vi "parsa" en fråga och lägga till i listan res
        res.append(parse_question(q))
    return res


def parse_answers(answers) -> list[Answer]:
    res = []
    for a in answers:
        res.append(Answer(a['answer'], a['correct']))
    return res


def parse_question(q) -> Question:
    return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], parse_answers(q['answers']))


if __name__ == '__main__':
    for question in get_questions():
        print(question.prompt)
        print(f"{question.percent_correct()} användare svarade rätt på frågan")
        for i, answer in enumerate(question.answers, start=1):
            print(f"[{i}] {answer}")

        print("-" * 80)
