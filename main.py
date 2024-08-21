"""This is a text-adventure."""

print("Entering forest")

PLAYER_HP = 100
MONSTER_HP = 10
PLAYER_ATTACK = 5
MONSTER_ATTACK = 1
WOOD = 0
X = 2

while X >1:
    print("What do you wanna do?")
    print("1: chop wood")
    print("2: fight monsters")
    z = input("Your action? \n")
    if z == "1":
        WOOD = WOOD + 1
        print(f"Wood storege is now {WOOD}")
    elif z == "2":
        while True:
            MONSTER_HP = MONSTER_HP - PLAYER_ATTACK
            print(f"Forester cut {PLAYER_ATTACK}")
            print(f"Monsters hp is: {MONSTER_HP}")
            if MONSTER_HP <= 0:
                print("Victory!!")
                break

            PLAYER_HP = PLAYER_HP - MONSTER_ATTACK
            print(f"Monster cut {MONSTER_ATTACK}")
            print(f"Your health is: {PLAYER_HP}")
