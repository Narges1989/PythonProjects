# TODO("Delete this 'TODO' and create your function here")
def fizz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 5 == 0:
        return 'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    else:
        return 'Foo'

#result = ''
# if number %3 ==0:
#     result += 'Fizz'
#
# if number % 3 == 0:
#     result += 'Buzz'
#
# if len(result) == 0:
#     result += 'Foo'

