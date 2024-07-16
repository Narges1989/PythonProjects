from to_do import TODO


def task11(assessments: str) -> str:
    result = assessments[3]
    return result

if __name__ == '__main__':
    # 'LLMHM', output = High
    print(task11('LLMHM'))

    # 'LLFFHMHF', output = Failure
    print(task11('LLFFHMHF'))