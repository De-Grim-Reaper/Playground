print("Hey buddy. This is a simple survey and i'd like to ask you a few questions... Do i have your consent?")
Ans = input("Yes/No: ")
Ans = Ans.lower()

while True:
    if Ans == "yes":
        print(
            "Well, let's get started...\n")
    elif Ans != "yes":
        print(
            "\nGo fuck yourself then.")
        break

    print("First question, What's your name?")
    Name = input()
    Name = Name.capitalize()

    while len(Name) == 0:
        Name = input("~Read the question and try again: \n")
        Name = Name.capitalize()

    print("Ok then {}, what's your favourite food?".format(Name))
    food = input()
    food = food.capitalize()

    while len(food) == 0:
        food = input("~Did i stutter?: \n")
        food = food.capitalize()

    print("Actually i don't give a fuck about your favorite food, i just wanted to be sure you're human."
          "But, {}?? Frs man? You ain't got taste.".format(food))
    print("That reminds me, what's your gender?\n")
    gender = input("Male/Female? \n")
    gender = gender.lower()

    while len(gender) == 0:
        gender = input("Male/Female? \n")
        gender = gender.lower()
    if gender == str("male"):
        print(
            "Tch. Was about to ask for your age but i don't really give a fuck."
            " Just tell me your age though i don't wanna be accused of being sexist")
    elif gender == str("female"):
        print(
            "Alr beautiful, can i have your phone no? ;). Just messing with ya, how old are you though? "
            "I know it's rude to ask but i ain't no pedophile")
    else:
        print(
            "Don't tell me you non-binary or something, i only got two types of gender in my dictionary shebro")

    quest = input("How old are you {}? ".format(Name))

    while quest[:10].isalpha() or len(quest) == 0:
        print("~Who taught you how to read?\n")
        quest = input("How old are you {}? ".format(Name))
    age = int(quest)

    if age >= 35 and gender == str("male"):
        print(
            "It was nice to have your cooperation in this survey sir, i don't bully old men. Have a nice day ;)")
    elif age >= 18 and gender == str("male"):
        print(
            "Well, like i said earlier... I don't give a fuck about your age. It's just part of this Survey.")
    elif age < 1 and gender == str("male"):
        print(
            "Lol, who's this fucker? Get outta here dumbass.")
    elif age <= 17 and gender == str("male"):
        print(
            "Tf you doing on my survey?! You ain't even got pubic hair yet, damn.")
    elif age > 50 and gender == str("female"):
        print(
            "Damn, you too old for this. Get outta here Granny!")
    elif age > 30 and gender == str("female"):
        print("Hehe, i actually don't have no experience with milfs, but there's a first for everything right? ;).")
        input(
            "Type in your phone number: ")
        print("Thanks, have a lovely day. I'll call you ;)")
    elif age >= 18 and gender == str("female"):
        print("Hehe, i hope you didn't lie about your age though... It ain't my fault if i get you preggs ;)")
        input("Type in your phone number: ")
        print(
            "Thanks, have a lovely day. I'll call you ;)")
    elif age < 1 and gender == str("female"):
        print(
            "Lol, who's this fucker? Get outta here dumbass.")
    elif age <= 17 and gender == str("female"):
        print(
            "Hell naw! Keep that phone number, i ain't a pedophile.")
    else:
        print(
            "You clearly don't know how to read.")
    break
