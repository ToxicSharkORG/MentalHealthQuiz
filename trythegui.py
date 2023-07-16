'''
import PySimpleGUI as sg
import pyttsx3
engine = pyttsx3.init()
layout = [[sg.Button('Click Me')]]
window = sg.Window("My Khidki", layout)
engine.setProperty('rate', 150)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Click Me':
        print('Button clicked!')
        engine.say("")
        engine.runAndWait()

window.close()
'''
import PySimpleGUI as sg

# GUI layout
layout = [[sg.InputText(key='input')],
          [sg.Button('Find Primes'), sg.Button('Exit')],
          [sg.Output(size=(100, 20))]]

# Create the window
window = sg.Window('Prime Number Finder', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Find Primes':
        try:
            limit = int(values['input'])
            primes = []
            for num in range(2, limit + 1):
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
            print(primes)
        except ValueError:
            print("Please enter a valid number.")

# Close the window
window.close()
