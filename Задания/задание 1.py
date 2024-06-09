import random

questions = {}

def add_question(question, answer):
    questions[question] = answer
    print(f"Вопрос '{question}' с ответом '{answer}' добавлен.")

def edit_question(question, new_answer):
    if question in questions:
        questions[question] = new_answer
        print(f"Ответ на вопрос '{question}' изменен на '{new_answer}'.")
    else:
        print(f"Вопрос '{question}' не найден.")

def delete_question(question):
    if question in questions:
        del questions[question]
        print(f"Вопрос '{question}' удален.")
    else:
        print(f"Вопрос '{question}' не найден.")

def get_random_question():
    if questions:
        random_question = random.choice(list(questions.keys()))
        return random_question, questions[random_question]
    else:
        return "Список вопросов пуст", ""

random_question, answer = get_random_question()
print(f"Случайный вопрос: {random_question}")
print(f"Ответ: {answer}")
