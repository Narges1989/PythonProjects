if __name__ == "__main__":
    sentence = "This has A number Of vowEls"
    letters_of_interest = ["a", "e", "i", "o", "u"]
    new_string = ""

    for letter in sentence:
        if letter.lower() in letters_of_interest:
            new_string += "$"
        else:
            new_string += letter

    print(new_string)
def transformer(sentence:str) -> str:
    letters_of_interest = ["a", "e", "i", "o", "u"]
    new_string = ""

    for letter in sentence:
        new_string += "$" if letter.lower() in letters_of_interest else letter

    return new_string
