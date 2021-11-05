import requests

from quiz2.data_model import Answer, Question

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


def get_questions(url: str) -> list[Question]:
    questions = requests.get(url).json()['questions']
    return [parse_question(q) for q in questions]


def parse_answer(a) -> Answer:
    return Answer(a['answer'], a['correct'])


def parse_answers(answers) -> list[Answer]:
    return [parse_answer(a) for a in answers]


def parse_question(q) -> Question:
    return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], parse_answers(q['answers']))


if __name__ == '__main__':
    for question in get_questions(QUIZ_URL):
        print(question.prompt)
        print(f"{question.percent_correct()} användare svarade rätt på frågan")
        for i, answer in enumerate(question.answers, start=1):
            print(f"[{i}] {answer}")

        print("correct answers")

        # Koden nedan skapar en lista med textsträngen answer från
        # alla svar på frågan question som är rätt
        print([a.answer for a in question.answers if a.correct])

        print("-" * 80)
