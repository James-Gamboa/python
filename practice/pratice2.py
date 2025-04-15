# make a program to convert text to morse code

def morse_code(user):
    dicc_morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                  "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                  "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                  "y": "-.--", "z": "--..",
                  "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                  "8": "---..", "9": "----.", "0": "-----", ", ": "--..--", ". ": ".-.-.-", "? ": "..--..", "/ ": "-..-.",
                  "- ": "-....-", "(": "-.--.", ")": "-.--.-"}
    return " ".join(dicc_morse[i] for i in user.lower())


user = input("Ingresa una frase: ")
print(morse_code(user))
