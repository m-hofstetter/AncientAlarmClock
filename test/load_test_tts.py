import unittest
from components.speaker import generate_speech

class LoadTest(unittest.TestCase):
    def test_load_tts(self):
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


if __name__ == '__main__':
    unittest.main()
