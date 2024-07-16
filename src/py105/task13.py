from to_do import TODO
import re

def task13(sentence: str) -> str:
    repeat_num_dict = {}
    sent_lower = sentence.lower()

    replace_list = [',', '!', '.', ';']
    # for i in replace_list:
    #     sent_lower = sent_lower.replace(i, '')
    #sent_lower = ''.join(filter(str.isalnum.sent_lower))
    sent_lower = re.sub('[,!.;]','',sent_lower)
    words = list(sent_lower.split())

    for word in words:
        if word not in repeat_num_dict.keys():
            repeat_num_dict[word] = words.count(word)

    max_repeat = 0
    for key, value in repeat_num_dict.items():
        if value> max_repeat:
            max_repeat = value
            max_word = key

    return max_word

if __name__== "__main__":
    print(task13('this, This; THIS, is still the very very same'))