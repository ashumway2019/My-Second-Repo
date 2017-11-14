print("What's your favorite musical?")
musical = input().lower()
if musical == "rent":
    print("The soundtrack is amazing. Who is your favorite character?")
    rent = input().lower()
    if rent == "mimi":
        print("Will you light my candle?")
    elif rent == "rodger":
        print("One song glory; one song before I go.")
    else:
        print(rent + " is a great character.")
elif musical == "dear evan hansen":
    print("The set was amazing. Who is your favorite character?")
    deh = input().lower()
    if "evan" in deh:
        print("He is my favorite character, too")
    if "jared" in deh:
        print("He is hilarious.")
elif musical == "hamilton":
    print("I love all the dancing and singing.")
elif musical == "grease":
    print("That is a classic.")
else:
    print(musical + " is probably a great musical.")
    




    
    
      
    
