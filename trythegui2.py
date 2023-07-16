import PySimpleGUI as sg
import pyttsx3

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
Mental health is a crucial aspect of overall well-being. It refers to our emotional,
 psychological, and social well-being, 
affecting how we think, feel, and act. Mental health is vital at every stage of life,
 from childhood and adolescence through adulthood.
Maintaining good mental health allows us to handle the challenges and stresses of life,
 have healthy relationships, and make meaningful 
contributions to our communities.
 It is important to prioritize mental health and seek support when needed.
This quiz aims to provide a general assessment of your mental well-being.
 Please answer each question honestly and on a scale of 1 to 100,
 with 1 being the least and 100 being the most severe.
'''
engine.say(intro_text)
engine.runAndWait()
# Create the GUI layout
layout = [
    [sg.Text(intro_text)],
    [sg.Button('Start Quiz')],
    [sg.Output(size=(60, 20), key='-OUTPUT-')]
]

# Create the window
window = sg.Window('Mental Health Quiz', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Start Quiz':
        # Clear the output area
        window['-OUTPUT-'].update('')

        # Questions and corresponding point values
        questions = {
            'question1': "On a scale of 1 to 100, how often have you been feeling down or depressed?",
            'question2': "On a scale of 1 to 100, how often do you get the feeling of being hopeless or worthless?",
            'question3': "On a scale of 1 to 100, how often do you have little interest or pleasure in doing things or find yourself procrastinating?",
            # Add more questions here
        }

        # Ask the user the questions and record their answers
        answers = {}
        for question, prompt in questions.items():
            engine.say(prompt)
            engine.runAndWait()
            while True:
                try:
                    answer = int(sg.popup_get_text(prompt + " (Enter a value from 1 to 100): "))
                    if 0 <= answer <= 100:
                        break
                    else:
                        sg.popup_error("Invalid answer. Please enter a value from 1 to 100.")
                except ValueError:
                    sg.popup_error("Invalid answer. Please enter a numeric value.")
            answers[question] = answer

        # Calculate the depression score
        score = calculate_depression_score(answers)

        # Categorize the depression level
        depression_level = categorize_depression_level(score)

        # Output the results
        sg.popup("Quiz Results:",
                 "Depression Score: " + str(score),
                 "Depression Level: " + depression_level)

        engine.say("Quiz Results:")
        engine.say("Depression Score: " + str(score))
        engine.say("Depression Level: " + depression_level)

        # Run TTS
        engine.runAndWait()

# Close the window
window.close()
