from to_do import TODO


def guide17(items: tuple[str]) -> list[str]:
    # result = []
    programming_files = ['kt','py','yml','json','java']
    # for pf in items:
    #     index = pf.split('.')
    #     if index[1] in programming_files:
    #         result.append(pf)
    # return result

    #return [pf for pf in items if pf.split('.')[1] in programming_files]

    return list(filter(lambda pf:pf.split('.')[1] in programming_files,items ))

if __name__== "__main__":
    # ["cv.pdf", "screenshot.png", "app.py", "main.kt", "thesis.pptx"] --> ["app.py", "main.kt"]
    print(guide17(["cv.pdf", "screenshot.png", "app.py", "main.kt", "thesis.pptx"]))