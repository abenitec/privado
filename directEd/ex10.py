print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There' s a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("l. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Offer the bear some honey")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("The bear is delighted by your offer and lets you share the cake.")
        print("Do you want to befriend the bear or escape while it's distracted?")
        print("1. Befriend the bear.")
        print("2. Escape.")

        friend = input("> ")

        if friend == "1":
            print("You and the bear become best buddies and go on many adventures together.")
            print("You win!")
        elif friend == "2":
            print("You sneak out of the room, but the bear notices and chases you down.")
            print("You lose!")
        else:
            print(f"Well, doing {friend} is probably better.")
            print("Bear runs away.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("l. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("4. You summon your courage and spit some fire at Cthulhu.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")

    elif insanity == "3":
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
    
    elif insanity == "4":
        print("You summon your courage and spit some fire at Cthulhu.")
        print("Do you speak in English or in Russian?")
        print("1. English.")
        print("2. Russian.")

        speak = input("> ")

        if speak == "1":
            print("Cthulhu is unimpressed by your weak rhymes and devours your soul.")
            print("You lose!")
        elif speak == "2":
            print("Cthulhu is amazed by your knowledge of his ancient tongue and spares your life.")
            print("You win!")
        else:
            print(f"Well, rapping in {speak} is probably better.")
            print("Cthulhu runs away.")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")