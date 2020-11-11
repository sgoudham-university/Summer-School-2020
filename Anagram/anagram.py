# Import libraries
from random import randint


def generate_anagram(word_list):
    """Rearrange the letters and return back the new anagram"""

    anagram = ""
    while len(word_list) > 0:
        random_index = randint(0, len(word_list) - 1)
        anagram += word_list[random_index]
        word_list.pop(random_index)
    return anagram


def main():
    """Generate an anagram with the given word"""

    word_list = list(input("Enter in the word that you want an anagram of:\n"))
    print(f"Anagram: {generate_anagram(word_list)}")


# Execute main method
main()
