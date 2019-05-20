import random
school = 7000
you = 500
en_hp = 2000
hit = 13
healLeft = 3
grenade = 6
HandGunShell = 72

print ("                         Welcome to The Save The School Game!")
print ("Oh No! Their Are bad guys In the School Being bados! Kill them!...")
print ("Decide what you want to do")
print ()
while True:
    move = input ("Enter [q] To chuck a grenade, [w] For Sniper, Enter [e] Hand Gun ~ Shoot The bados, [r] To 1v1 one guy [t] to heal")
    print ("_______________________________________________________________________________")
    if move == 'q':
        if grenade > 0: 
            print ("BOOM!")
            grenade -= 1
            if hit < random.randint(0,1000):
               school -= random.randint(93,1000)
               en_hp -= random.randint(50,200)
               print("You did", school, "damage to School")
               print("You did", en_hp, "Bad guys health")
        else:
            print("[No more grenades!]")
        print ("_______________________________________________________________________________")
    elif move == 'w':
        print ("︻デ┳═ー")
        if hit < random.randint(170,200):
            rnd = random.randint(170,200)
            en_hp -= rnd
            if rnd > 190:
                print("Headshot")
                print("          Bad guys health:", en_hp)
            else:
                print("You hit them for", rnd, "HP!")
                print("Sniper")
                print("          Bad guys health:", en_hp)
                print ("_______________________________________________________________________________")
                print()
    elif move == 'e':
        if HandGunShell > 0:
            print ("̿' ̿'\̵͇̿̿\ ")
            HandGunShell -= 1
            if hit < random.randint(50,120):
                you -= random.randint(0,50)
                en_hp -= random.randint(0,100)
                print("          Your health:", you)
                print("          Bad Guys health:", en_hp)
            else:           
                print("[No Ammo Left!]")
                print("          Your health:", you)
                print("          Bad Guys health:", en_hp)
                print ("_______________________________________________________________________________")
                print()
        else:
            print("[No Ammo Left!]")
            print ("_______________________________________________________________________________")
            print()
    elif move == 'r':
        print ("1v1! ")
        if hit < random.randint(0,56):
            en_hp -= random.randint(20,80)
            you -= random.randint(20,80)
            print("          Your health:", you)
            print("          Bad Guys health:", en_hp)
        else:           
            print("Now USE Your Hands!")
            print("          Your health:", you)
            print("          Bad Guys health:", en_hp)
            print ("_______________________________________________________________________________")
            print()

    elif move == 't':
        if healLeft > 0:
            print ("Heal")
            healLeft -= 1
            if hit < random.randint(100,200):
                you += random.randint(100,200)
                print("          Your health:", you)
                print("          Bad Guys health:", en_hp)
            else:           
                print("Heal")
                print("          Your health:", you)
                print("          Bad Guys health:", en_hp)
                print ("_______________________________________________________________________________")
                print()
        else:
            print("[No heals left!]")
            print ("_______________________________________________________________________________")
            print()
    else:
        print("Invalid")
            
            
    if en_hp <= 0: 
        print("        ☆★☆★")
        print ("You SAVED THE School :D")
        print("        ☆★☆★")
        break
    elif you <=0:
        print ("†")
        print ("Your Dead!")
        print ("†")
        break
    elif school <0:
        print ("YOU Kill The School!   D:")
        break
    

