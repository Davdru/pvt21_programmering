from quiz2.api import QuizAPI, BaseAPI
from random import randint


QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


class Player:
    def ask_num(self, n):
        raise NotImplementedError


class ConsolePlayer(Player):
    def ask_num(self, n):
        while True:
            res = int(input(">"))
            if 1 <= res <= n:
                return res


class DummyPlayer(Player):
    def ask_num(self, n):
        return randint(1, n)


class QuizGame:
    quiz_api: BaseAPI
    player: Player

    def __init__(self, quiz_api: BaseAPI, player: Player):
        self.quiz_api = quiz_api
        self.player = player

    def run(self):
        for question in self.quiz_api.get_questions():
            print(question.prompt)
            print(f"{question.percent_correct()} användare svarade rätt på frågan")
            for i, answer in enumerate(question.answers, start=1):
                print(f"[{i}] {answer}")
            user_answer = self.player.ask_num(question.num_answers)
            print(f"User answered {user_answer}")

            # Koden nedan skapar en lista med textsträngen answer från
            # alla svar på frågan question som är rätt
            # print([a.answer for a in question.answers if a.correct])

            print("-" * 80)


if __name__ == '__main__':
    q_api = QuizAPI(QUIZ_URL)
    p = DummyPlayer()
    quiz = QuizGame(q_api, p)
    quiz.run()
