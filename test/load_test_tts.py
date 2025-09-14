from time import sleep

from components.speaker import generate_and_say, generate_speech

i = 0
while i < 100:
    human_rights = '''
    Alle Menschen sind frei und gleich an Würde und Rechten
    geboren. Sie sind mit Vernunft und Gewissen begabt und
    sollen einander im Geist der Solidarität begegnen.
    '''
    print(i, "/100")
    i = i + 1
    generate_speech(human_rights)
    sleep(0.5)

