from to_do import TODO


def task14(sentence: str) -> str:
    sent_lower = sentence.lower()

    replace_list = [',', '!', '.', ';',' ']
    for i in replace_list:
        sent_lower = sent_lower.replace(i, '')

    repeated_characters_dict = {}
    for letter in sent_lower:
        repeated_characters_dict[letter] = sent_lower.count(letter)

    max_repeat = 0
    for key, value in repeated_characters_dict.items():
        if value > max_repeat:
            max_repeat = value
            max_letter = key

    return max_letter

if __name__ == "__main__":
    print(task14('Pa: na. ma;'))
