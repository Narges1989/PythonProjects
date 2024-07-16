from to_do import TODO


def guide9(email: str) -> bool:
    if (email != '') and (email.count('@') != 0) and (email[-3:] =='.se'):
        return True
    else:
        return False

if __name__ == "__main__":
    # email = '', output = False
    print(guide9(''))

    # email = 'studentlinerotech.se', output = False
    print(guide9('studentlinerotech.se'))

    # email = 'student@linerotech.com', output = False
    print(guide9('student@linerotech.com'))

    # email = 'student@linerotech.se', output = True
    print(guide9('student@linerotech.se'))
