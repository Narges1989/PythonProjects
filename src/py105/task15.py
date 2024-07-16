import string

from to_do import TODO


def task15(sentence: str) -> dict[str, int]:
    repeat_letter_dict = {}
    sent_lower = sentence.lower()
    replace_list = [',', '!', '.', ';']
    for i in replace_list:
        sent_lower = sent_lower.replace(i, '')
    sent_lower = string.punctuation()

    words = list(sent_lower.split(' '))
    first_letter = []
    for word in words:
        first_letter.append(word[0])

    for letter in first_letter:
        if letter not in repeat_letter_dict.keys():
            repeat_letter_dict[letter] = first_letter.count(letter)

    return repeat_letter_dict

if __name__ == "__main__":
    print(task15('This is the Very small Text'))