from to_do import TODO


def task12(assessments: str) -> str:
    temp = int(len(assessments)/2)
    result = assessments[temp]
    return result

if __name__ == '__main__':
    # 'LLMHM', output = M
    print(task12('LLMHM'))

    # 'LLFFHLMHF', output = H
    print(task12('LLFFHLMHF'))