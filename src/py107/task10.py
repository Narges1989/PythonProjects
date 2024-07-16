# TODO("Delete this 'TODO' and create your function here")
def tweet(text: str) -> str:
    end_of_text = (280 - len(text)) * '@'
    return text + end_of_text