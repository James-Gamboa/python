# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words():
    text = input("Ingresa una frase: ")

    words = text.split(" ")

    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    result = " ".join(reversed_words)

    print(result)


reverse_words()
