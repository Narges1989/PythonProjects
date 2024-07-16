def single_error():
    raise KeyError


def create_password(password: str):
    if len(password) < 3:
        raise AssertionError("Password is too short")
    elif password == "qwerty":
        raise NameError("Invalid password name. Too Easy")
    elif password[0] == "q":
        raise SystemError("Unable to create password")
    else:
        print("Password created successfully")


def get_file_details(filename: str):
    if filename.lower() == "python":
        print(f"File Content --> Python is amazing")
    elif filename.lower() == "kotlin":
        print(f"File Content --> Kotlin is amazing")
    else:
        raise FileNotFoundError(f"'{filename}' was not found")


if __name__ == "__main__":
    # assert keyword: to make sure that conditions are true otherwise stop the app
    # for senario with a import condition that if it was not valid, program should not continue
    user_age = int(input('what is your age?'))
    assert(user_age>17)
    print('you are adult')

    # raise keyword: manually trigger an exception
    filenames = ['app.py','run.py','main.py']
    user_filename = input('provid me with a filename')
    # assert(user_filename in filenames)
    if user_filename not in filenames:
        raise FileNotFoundError(f"The file '{user_filename}' was not found")
    else:
        print('The file was found')





    # print('--- Start ---')
    # try:
    #     file_name = input('please Enter a filename:')
    #     print('Open DataBase')
    #     get_file_details(file_name)
    # except FileNotFoundError:
    #     print('Unable to get File details')
    # else: # Only when excutes that try executed successfully
    #     print('Operation Completed without any problem')
    # finally: # finally executes regardless of which try or except was executed
    #     print('Close DataBase')


    print('---END----')




    # # Handling RunTime Error: when you would like to run a code a little bit risky you can use try exception
    # print('start')
    # try:
    #     filename = input('Enter a filename')
    #     get_file_details(filename)
    # except FileNotFoundError: # just handles File not found error, if any other error happens this exception can not handle
    #     print('Unable to get file details')

    # Handling multiple run-time errors
    # try:
    #     user_password = input('Enter your password:')
    #     create_password(user_password)
    # except AssertionError:
    #     print('your password is too short')
    # except NameError:
    #     print('password is too easy')
    # except SystemError:
    #     print('unabel to connect to server, try again after a while')


    # Syntax Error
    # Errors occurs when syntax rules are broken ->
    # rules are about writing words correctly
    # print(name -> this is a syntax error (forgetting close paranthesis)

    # Index error
    letters = ['a','b','c']
    # print(letters[10]) this is the index error because there is not index 10 in the list

    # Key Error
    data = {'one':1,'two':2,'three':3}
    # print(data['four'])  this is the key error

    # Zero Division error
    # print(10/0) this error when happens that you wanted divide a arbitary number by 0

    # with these errors, application  doesnt start running of stop running


    # Type of Errors: Errors can be categorized in one of these 3 types:
    # type 1. Logical Error: Program finishes executing successfully but does not provide the expected behaviour
    print('--- START ---')
    countries = ['Panama', 'Sweden', 'Norway']
    print(countries[1]) # we wanted to print Panama instead of Sweden
    print('--- END ---')

    # type 2. Runtime Error: The program begins executing but stops abruptly before successfully completing execution
    print('--- START ---')
    # single_error()
    # For example: key error, zero division error, index error
    print('--- END ---')

    # type 3. Compile Time Error: The program does not start running
    # python is not a compiled program, it is an interpreter programming language
    # syntax error
    print('--- START ---')
    #name 'Humberto'
    #print(name)
    print('--- END ---')








