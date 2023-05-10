import json
import random


def generate_questions(num_questions=1000):
    categories = ["""history""", """science""", """geography""", """literature""", """music""", """movies""", """sports"""]
    difficulty_levels = ["""easy""", """medium""", """hard"""]
    questions = []

    for i in range(num_questions):
        category = random.choice(categories)
        difficulty = random.choice(difficulty_levels)
        question = f"""What is the
        {difficulty}
        {category}
        question
        {i + 1}?"""
        answers = [f"""Answer {i + 1} - 1""", f"""Answer {i + 1} - 2""", f"Answer {i + 1} - 3", f"Answer {i + 1} - 4"]
        correct_answer = random.choice(answers)

        questions.append({
            """question""": question,"""answers""": answers,"""correct_answer""": correct_answer,"""category""": category,"""difficulty""": difficulty})

        with open("""questions.json""", """"w""") as f:
            json.dump(questions, f)