from to_do import TODO


def task13(assessments: str) -> str:
    result = assessments[0:3]
    return result

if __name__ == '__main__':
    # 'LLMHM', output = LLM
    print(task13('LLMHM'))

    # 'LLFFHLMHF', output = LLF
    print(task13('LLFFHLMHF'))