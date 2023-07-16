import pyttsx3
import PySimpleGUI as sg
def calculate_depression_score(answers):
    score = sum(answers.values())  # Sum all the answer values

    return score


def categorize_depression_level(score):
    if score <= 20:
        return "1 - Healthy"
    elif score <= 40:
        return "2 - Mild depression"
    elif score <= 60:
        return "3 - Moderate depression"
    elif score <= 80:
        return "4 - Severe depression"
    else:
        return "5 - Very severe depression"


# TTS initialization
engine = pyttsx3.init()

# Introduction and essay on mental health
intro_text = '''
Welcome to the Mental Health Quiz!
Mental health is a crucial aspect of overall well-being. It refers to our emotional, psychological, and social well-being, affecting how we think, feel, and act. Mental health is vital at every stage of life, from childhood and adolescence through adulthood.
Maintaining good mental health allows us to handle the challenges and stresses of life, have healthy relationships, and make meaningful contributions to our communities. It is important to prioritize mental health and seek support when needed.
This quiz aims to provide a general assessment of your mental well-being. Please answer each question honestly and on a scale of 1 to 100, with 1 being the least and 100 being the most severe.
'''
print(intro_text)
engine.say(intro_text)
engine.runAndWait()

# Questions and corresponding point values
questions = {
    'question1': "On a scale of 1 to 100, how often have you been feeling down or depressed?",
    'question2': "On a scale of 1 to 100, how often do you get the feeling of being hopeless or worthless(that is a complete lie, you are very important to the people around you)?",
    'question3': "On a scale of 1 to 100, how often do you have little interest or pleasure in doing things or find yourself procrastinating?",
    'question4': "On a scale of 1 to 100, how often have you had trouble falling asleep, staying asleep, or sleeping too much?",
    'question5': "On a scale of 1 to 100, how often do you have the days when you have very low/no energy?"
}

# Ask the user the questions and record their answers
answers = {}
for question, prompt in questions.items():
    engine.say(prompt)
    engine.runAndWait()
    answer = int(input(prompt + " (Enter a value from 1 to 100): "))
    if answer>100:
        print("Your answer Should only be from 1 to 100, and not exceed 100 to be correctly evaluated, please answer again")
        answer = int(input(prompt + " (Enter a value from 1 to 100): "))
    answers[question] = int(answer)

# Calculate the depression score
score = calculate_depression_score(answers)

# Categorize the depression level
depression_level = categorize_depression_level(score)

# Output the results
print("\n--- Quiz Results ---")
print("Depression Score: ", score)
print("Depression Level: ", depression_level)

engine.say("Quiz Results:")
engine.say("Depression Score: " + str(score))
engine.say("Depression Level: " + depression_level)

# Run TTS
engine.runAndWait()
