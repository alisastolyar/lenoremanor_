import time

answer_a = ["A", "a", "Yes", "yes", "Y", "y"]
answer_b = ["B", "b", "No", "no", "N", "n"]

required = ("\nYou can only choose option A or B, OR yes or no.\n")

print("Welcome to your doom… Can you survive the abandoned Lenore Manor?...\n\n")

def enter():
    print("After you walk in, you can either turn left or go into the basement in front of you.\n")
    time.sleep (1)
    choice = input("""
        A. Go left
        B. Basement
        \n>>>""")

    if choice in answer_a:

        print("""You turn left and the room in front of you is unusually dark.
Suddenly, a candle flickers on by itself and the hair on the back
of your neck raises as you feel a cold breeze blow from behind you.
You turn around and don’t see the entryway that you came from; only darkness.
You turn back around to face the single burning candle and see an old man
appear holding the candle. He is wearing an old suit covered in ash; his face
is covered in burns, to the point where you can’t tell what he looks like.
Due to his translucency, you realize that he is not human and you start to panic.
Before you can make the split decision to run, the old man drops the candle and
the room catches on fire. You realize there is nowhere for you to run so you get as
far away from the flames as you can. The man watches you from across the room,
waiting for you to suffer the same death that he did.\n""")
        time.sleep (15)
        print("GAME OVER\n")
        raise SystemExit

    elif choice in answer_b:
            print("""As you reach the bottom of the stairs, the second to last stair breaks in
and you fall forward. When you look back, you see that there was an old wooden box
inside of the step. You open it and see a key with a note: “Check the red door at your own risk.”\n""")
            time.sleep (2)

    else:
        print(required)
        time.sleep(1)
        enter()

def part2():
    print("Do you use the key?\n")
    time.sleep(0.75)
    choice2 = input("""
    A. Yes, I’ll go looking for the red door.
    B. No, I don’t want to take the risk.
    \n>>>""")

    if choice2 in answer_a:
        print("""You find the red door behind broken wallpaper. You reluctantly open
the door with the key and wave away the spiderwebs that block your path.
You see a portrait of a young man in the back of the closet. A translucent
figure pops out of the frame and warns you to not look upstairs. \n""")
        time.sleep(1)

    elif choice2 in answer_b:
        print("""You run out of the closet and run toward the ballroom. Ahead of you
is a grand piano, and it starts playing what sounds like Bach. The playing
gets louder and louder and the whole room starts shaking. The chandelier
starts breaking and is about to fall to the ground, shattering. You look back at the piano,
trying to figure out a way to stop it. A headless man in a suit appears on the seat.
You run toward the door out of the ballroom as fast as you can, but you’re not fast enough.
The crystal chandelier breaks from the ceiling and lands on top of you. The music calms
down to its previous volume and the headless man is no longer there. You didn’t make it. \n""")
        time.sleep(10)
        print("GAME OVER\n")
        raise SystemExit

    else:
        print(required)
        time.sleep(1)
        part2()


def part3():
    print("Do you look upstairs?\n")
    time.sleep(0.75)
    choice3 = input("""
    A. Yes
    B. No
    \n>>>""")

    if choice3 in answer_a:
        print("""You walk up the creaky stairs, holding your flashlight as tight as you can.
You reach the top and are met with a long hallway with a porcelain doll sitting at the end.
You try to pick up the doll, but it feels like an anvil. The doll starts floating and you
start crawling backwards. Suddenly, the doll whispers “follow me” in a childish voice and
starts floating by the last door on the right, covered in cobwebs. You slowly get up, half
paralyzed from fear, and walk toward the door. The doll floats behind you as you open the door.
After you open the door, you feel a small push from behind you. You fall forward into pure darkness
for what seems like forever. Your violent screams echo around you, melding with the childish laughter
from the doll floating above. The porcelain doll stands over the bottomless pit, watching you fall
deeper and deeper into your insanity.\n""")
        time.sleep(15)
        print("GAME OVER\n")
        raise SystemExit

    elif choice3 in answer_b:
        print("""You walk into the living room and see a desk at the far end. You sit in the chair
and suddenly it turns with you in it. You are now facing the bookshelf. You see a bright
emerald book on the shelf in front of you. You jokingly wonder if the shelf is a secret door,
so you pull at the book to see. The chair turns quickly with the bookshelf into the other room.
You’re pale as a ghost when you see a door at the end of a very long corridor with screams
coming from it. You walk slowly toward the door and the screams get louder and louder.
You see countless scratch marks on the walls and blood spattered on the floor.\n""")

    else:
        print(required)
        time.sleep(1)
        part3()


def part4():
    print("Do you open the door?\n")
    time.sleep(0.75)
    choice4 = input ("""
    A. Yes
    B. No
    \n>>>""")

    if choice4 in answer_a:
        print("""You step right in front of the door. The temperature drops and you cross your arms
to fight the cold. You reach for the handle and suddenly the door disappears. You start to
panic and look behind you. You run toward the door that you came from, but the chair and
the bookshelf are both gone. The screams continue and get louder. Before you know it,
you’re screaming too and can’t stop.\n""")
        time.sleep(10)
        print("GAME OVER\n")
        raise SystemExit

    elif choice4 in answer_b:
        print("""You sprint back to the chair and try to pull at the book again but this time the book
comes right off of the shelf. You think you’re trapped but the book starts heating up to the point
that you drop it on the floor. A small fire burns words in the book and then goes out.
You pick up the book and spelled out in ashen letters is a message: “Oopsie.” You’re confused for a moment,
but then the chair falls through the floor and you land hard on the ground. You never went to another floor,
yet you find yourself sitting in the entryway where you entered the manor. You see a sign on the door,
written in blood: “Leave and never come back.”\n""")

    else:
        print(required)
        time.sleep(1)
        part4()

def part5():
    print("Do you leave?\n")
    time.sleep(0.75)
    choice5 = input("""
    A. Yes
    B. No
    \n>>>""")

    if choice5 in answer_a:
        print("""You stand up and open the heavy front door, then proceed to run for your life.
You run until you can’t feel your feet as they hit the ground. You stop to look back,
only to see a empty hill with no trace of the manor. You’re confused, but at least you survived.\n""")
        time.sleep(3)
        print("YOU WIN\n")
        raise SystemExit

    elif choice5 in answer_b:
        print("""You decide to keep investigating. You stand up and rub your head from the fall.
You take a few steps toward the grand kitchen, and feel the house start rumbling.
You run for the door, but it won’t open no matter how hard you try. The manor starts
falling in on itself and you hear deep laughter bounce off the walls. There is no way out.
You didn’t make it.\n""")
        time.sleep(1)
        print("GAME OVER\n")
        raise SystemExit

    else:
        print(required)
        time.sleep(1)
        part5()

enter()
part2()
part3()
part4()
part5()
