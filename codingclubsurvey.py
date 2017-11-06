while True:
    print ("Are you in coding club?")
    club = input().lower()
    if club == "yes":
        print("What's your advisory?")
        advisory = input().lower()
        if advisory == "kast":
            print("Hey Alexa!")
            break
        elif advisory == "moore":
            print("Do you take field hockey?")
            sport = input().lower()
            if sport == "yes":
                print("You are Lyla.")
                break
            elif sport == "no":
                print("You are Ella.")
                break
        elif advisory == "rosenberg":
            print("You are Madison.")
            break
        elif advisory == "spencer":
            print("Do you play lacrosse?")
            lacrosse = input().lower()
            if lacrosse == "yes":
                print("You are Annie.")
                break
            if lacrosse == "no":
                print("You are Anna.")
                break
        elif advisory == "mcglynn":
            print("You are Milli.")
            break
        elif advisory == "preston":
            print("you are Lauren.")
            break
        else:
            print("You are Mr. Rosenfeld.")
            break
    elif club == "no":
        print("Oh, this survey is meant for people in coding club.")
        break
    else:
        print("Please answer with yes or no.")

    
    
