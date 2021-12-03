import requests
from http import HTTPStatus


QUIZ_URL = "https://bjornkjellgren.se/quiz/v1/questions"


class APIError(Exception):
    pass


def get_questions() -> dict:
    res = requests.get(QUIZ_URL)
    if res.status_code == HTTPStatus.OK:
        return res.json()
    else:
        raise APIError(f"Quizz api responded with {res}")


def ask_question(q: dict) -> bool:
    print(q['prompt'])
    i = 1
    for a in q['answers']:
        print(f"{[i]} {a['answer']}")
        i += 1
    user_ans = int(input(">"))
    return q['answers'][user_ans-1]['correct']


def main():
    questions = get_questions()
    score = 0
    num_questions = 0
    for question in questions['questions']:
        num_questions += 1
        if ask_question(question):
            score += 1

    print(f"Du fick {score} rätt av {num_questions} möjliga")


if __name__ == '__main__':
    main()
