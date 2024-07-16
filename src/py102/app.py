if __name__ == "__main__":
    first_name = "Humberto"
    last_name = "Linero"
    country = "Panama"
    language = "Spanish"

    # method #1: Ugly method for string concatenation
    sentence = "Hello "+ first_name+ " " + last_name+"you come from "+country+" and you speak "+language
    print(sentence)

    # method #2: f-string (f= format)
    sentence2 = f"Hello {first_name} {last_name} you come from {country} and you speak {language}"
    print(sentence2)