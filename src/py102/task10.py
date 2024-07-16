from to_do import TODO


def task10(assessments: str) -> int:
    result = len(assessments)
    return result

if __name__ == '__main__':
    # 'LLMHM', output = 5
    print(task10('LLMHM'))

    # 'LLHMHF', output = 8
    print(task10('LLFFHMHF'))