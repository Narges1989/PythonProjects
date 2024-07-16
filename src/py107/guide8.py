#if __name__ == "__main__":
    # sentence = "I want to visit Hawaii, Hungary, and Honduras"
    # positions = []
    #
    # for index, letter in enumerate(sentence):
    #     if letter == "H":
    #         positions.append(index)
    #
    # print(positions)
    #
# def finder_H(letter):
#     return letter=='H'
# def indexer(sentence,finder_H):
#     positions = []
#     for index, letter in enumerate(sentence):
#          if finder_H(letter):
#              positions.append(index)
#     return positions


def indexer(sentence:str) -> list[int]:
   return [index for index, letter in enumerate(sentence) if letter == "H"]

print(indexer("I want to visit Hawaii, Hungary, and Honduras"))


