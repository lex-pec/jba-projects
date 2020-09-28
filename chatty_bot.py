question = """
Here's an (unfinished) while loop:
x = 25
while ___:
    print(x)
    x += 3
Instead of the underscores put the condition which will produce the biggest amount of output:
1. x % 2 != 0
2. x*2 % 100 >= 50
3. x > 0
4. x <= 30
"""


def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print(question)
    answer = int(input())
    while answer != 3:
        print('Please, try again.')
        answer = int(input())
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Helper', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
