'''
x = "Scantlin."
if x.endswith("."):
    x = x[:-1]
print(x)
#the output is Scantlin because the period is removed
'''
#Quiz game in python
'''
def quiz_game(name):
    print(f"Welcome to our mini quiz game {name}")
    score = 0
    questions = {"What is the largest organ of human?": "skin",
             "What is the 3rd planet in solar system?": "earth",
             "also known as red planet?": "mars",
             "Java released on what year?": "1995"}
    
    for i, (questions, answers) in enumerate(questions.items()):
        print(questions)

        user = input("Enter your answer: ").lower()
        while user != answers:
            print("try again")
            print(questions)
            user = input("Enter your answer: ")

        print("Congratulations, you've got it right")
        score += 1

    return f"you've got {score}/4"

print(quiz_game(input("Enter your name: ")))
'''
'''
def diamond(raws):
    for i in range(raws + 1):
        print((" " * (raws-i)) + (" *" * (i)))
    for i in range(1, raws):
        print((" " * i) + (" *" * (raws-i)))

diamond(10)
'''

for i in range(2, 20, 2):
    print(i)
