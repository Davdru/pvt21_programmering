import random
import requests


class Answer:
    answer: str
    correct: bool

    def __init__(self, answer: str, correct: bool):
        self.answer = answer
        self.correct = correct


class Question:
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list[Answer]

    def __init__(self, id: int, prompt: str, times_asked: int, times_correct: int, answers: list[Answer]):
        self.id = id
        self.prompt = prompt
        self.times_asked = times_asked
        self.times_correct = times_correct
        self.answers = answers


# API skall fungera som ett interface.
# Det betyder att vi här beskriver vilka metoder
# som ett API i vårt program skall ha.
# Det är inte tänkt att man skall instansiera och använda
# klassen API direkt, istället skall vi implementera
# en eller flera subklasser.
# För att säkerställa att API inte används direkt
# ser vi till att metoderna ger ett exception när dom används
class API:
    def get_questions(self) -> list[Question]:
        raise NotImplementedError

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError


class User:
    def ask_question(self, question: Question) -> Answer:
        raise NotImplementedError


class WebAPI(API):
    url: str

    def __init__(self, url: str):
        self.url = url

    def get_questions(self) -> list[Question]:
        questions = []
        for question in requests.get(self.url).json()["questions"]:
            # Först hämtar vi upp alla fält från en fråga
            id = int(question["id"])
            prompt = question["prompt"]
            times_asked = int(question["times_asked"])
            times_correct = int(question["times_correct"])

            # Nästa problem är svarsalternativen, som ligger i en lista
            # Vi behöver läsa in dom, skapa instanser av Anser och lägga i en lista
            answers = []
            for answer in question["answers"]:
                ans = answer["answer"]
                correct = answer["correct"]
                answers.append(Answer(ans, correct))

            questions.append(Question(id, prompt, times_asked, times_correct, answers))
        return questions

    # Inte implementerad än, testa att lägga till kod som faktiskt skickar data till apiet
    def post_answer(self, question: Question, correct: bool):
        print(f"Post answer{question.prompt}, correct {correct}")


# En implementation av User som skriver ut frågan i konsollen
# och frågar användaren efter ett svar
# Kan förbättras genom felhantering av det användaren matar in
# Skriv en hjälpfunktion som hämtar in ett svar från användare
# skall bara acceptera giltiga heltal
class ConsoleUser(User):
    def ask_question(self, question: Question) -> Answer:
        print(question.prompt)
        for i, ans in enumerate(question.answers):
            print(f"{i}: {ans.answer}")

        user_anser = int(input(">"))
        return question.answers[user_anser]


# Den här användare svarar automatiskt rätt på alla frågor
class CheatingUser(User):
    def ask_question(self, question: Question) -> Answer:
        print(question.prompt)
        for i, ans in enumerate(question.answers):
            print(f"{i}: {ans.answer}")

        for i, ans in enumerate(question.answers):
            if ans.correct:
                print(f"Answering {i}")
                return ans


class Quiz:
    api: API
    user: User
    __questions: list[Question]

    def __init__(self, api: API, user: User, max_num_questions: int):
        self.api = api
        self.user = user
        self.__questions = random.sample(self.api.get_questions(), max_num_questions)

    def run(self):
        score = 0
        for question in self.__questions:
            ans = self.user.ask_question(question)
            if ans.correct:
                score += 1
                print("Correct!")
            else:
                print("Wrong!")
            self.api.post_answer(question, ans.correct)

        print(f"You got a score of {score}")


if __name__ == '__main__':
    api = WebAPI("https://bjornkjellgren.se/quiz/v2/questions")
    user = ConsoleUser()
    quiz = Quiz(api, user, 5)
    quiz.run()
