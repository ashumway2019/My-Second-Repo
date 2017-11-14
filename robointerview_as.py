def question(q):
    global answer
    answer = input(q)
    print(answer)

    
question("What's your name?")

question("What is your favorite class?")
question("What are you learning now in " + answer + "?")

question("What are your favorite extracurricular activities?")
question("How often do you do " + answer + "?")
    if answer == "15 hours a week":
        print("Wow, that's a lot of activities.")
    else:
        print("Fun.")

question("What book have you read recently?")

question("What are your academic personal strengths and weaknesses?")
