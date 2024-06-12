# Your solution to Exercise 18

name = input("Remember the name: ").lower()

if name == "yes":
    ex = input("Is it an ex: ").lower()
    if ex == "yes":
        drunk = input("Are you drunk: ").lower()
        if drunk == "yes":
            rekindle = input("Do you want to rekindle: ").lower()
            if rekindle == "yes":
                print("Say hi.")
            elif rekindle == "no":
                print("Don't say hi.")
        elif drunk == "no":
            convertible = input("Are you in a convertible with Brad Pitt and/or Rhianna: ").lower()
            if convertible == "yes":
                print("Say hi.")
            elif convertible == "no":
                print("Don't say hi.")
    elif ex == "no":
        friend_ex = input("A friend's ex: ").lower()
        if friend_ex == "yes":
            print("Don't say hi.")
        elif friend_ex == "no":
            enemy = input("An enemy or frenemy: ").lower()
            if enemy == "yes":
                convertible = input("Are you in a convertible with Brad Pitt and/or Rhianna: ").lower()
                if convertible == "yes":
                    print("Say hi.")
                elif convertible == "no":
                    print("Don't say hi.")
            elif enemy == "no":
                bank = input("Are you robbing a bank: ").lower()
                if bank == "yes":
                    print("Don't say hi.")
                elif bank == "no":
                    bathrobe = input("Are you in a bathrobe: ").lower()
                    if bathrobe == "yes":
                        print("Don't say hi.")
                    elif bathrobe == "no":
                        print("Say hi.")
elif name == "no":
    flee = input("Is there time to flee: ").lower()
    if flee == "yes":
        print("Run for it.")
    elif flee == "no":
        call = input("Could you pretend to get a call on your cell: ").lower()
        if call == "yes":
            print("Hello, doctor. What are my test results?")
        elif call == "no":
            sunglasses = input("Are you wearing sunglasses: ").lower()
            if sunglasses == "yes":
                print("Keep walking.")
            elif sunglasses == "no":
                print("Address the person using an amusing nickname such as""Sarge,""Slugger,""or""Master Blaster.")
else:
    print("Try again.")