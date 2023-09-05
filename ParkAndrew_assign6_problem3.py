import digitalnum
import random
#create repeating while loops to keep asking until user gives a valid input
while True:
    problems = int(input("How many problems would you like to solve? "))
    if problems <= 0:
        print("Invalid number, try again")
        print()
    else:
        break
while True:
    width = int(input("How wide do you want your digits to be? 5-10: "))
    if width < 5 or width > 10:
        print("Invalid width, try again")
    else:
        break
while True:
    character = input("What character would you like to use? ")
    if len(character) < 1 or len(character) > 1:
        print("String too long, try again")
    else:
        print()
        print("Here we go!")
        break
#set limiter variable
correct = 0
#keep asking problems based on the amount of problems user enter
for i in range(problems):
    print()
    print("What is .....")
    print()
    #randomly select numbers
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    operator = random.randint(1,2)
    #if op == 2, use + else, use -
    if operator == 2:
        digitalnum.print_number(num1, width, character)
        print()
        print(digitalnum.plus(5, character))
        print()
        digitalnum.print_number(num2, width, character)
        print()
        ans = int(input("= "))
        answer1 = digitalnum.check_answer(num1, num2, ans, "+")
        if answer1 == True:
            print("Correct!")
            correct += 1
        else:
            print("Sorry that is incorrect")
    else:
        digitalnum.print_number(num1, width, character)
        print()
        print(digitalnum.minus(5, character))
        print()
        digitalnum.print_number(num2, width, character)
        print()
        ans = int(input("= "))
        answer1 = digitalnum.check_answer(num1, num2, ans, "-")
        if answer1 == True:
            print("Correct!")
            correct += 1
        else:
            print("Sorry that is incorrect")       

print()
print("You got", correct, "out of", problems, "correct!")






