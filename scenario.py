player_name = input("Enter your name")
health = 100
location = "building"
situation = "panicked"

health-= 25 #player health loses
print(f"You woke up in your small apartment and noticed that you see a dark smoke outside.")
print(f"You checked and realized that your apartment building is on fire!")
print(f"You panicked, the apartment is getting hotter every second. Smokes creeps outside your window.")
print(f"All of the sudden the ceiling collapsed on you leaving you with a health of {health}")

def show_status(player_name, health, location, situation):
    print(f"Health: {health}")
    print(f"Location: {location}")
    print(f"Situation: {situation}")

show_status(player_name, health, location, situation)

print(f"You went outside your apartment, trying to find a way. You see the stairs full of debris, it looks unsafe. ")
choice = input("Do you wish to use the stair (a) or find another way (b)? ")
if choice == 'a':
    health -= 30
    print("The fire got worse near the stairs and lost some health.")
elif choice == 'b':
    location = 'Hallway'
    print(f"You chose to find another way that is safe.")
else:
    print("Invalid choice. you're trying to get out. the longer you stay your health will decrease.")
    health -=20
    location = 'Hallway'

show_status(player_name, health, location, situation)

choice = input("You saw the fire escape stair do you wish to use it (c) or find another way (d)? ")
if choice == 'c':
    print("You have escaped the building and the emergency response team treated you.")
    health += 25
    location = 'Safe'
    situation = 'Youre safe and sound'
elif choice == 'd':
    print(f"You chose not to use the stair, you missed your chance and got stuck at the building unable to get out.")
    location = 'Inside the building'
    situation = 'Unable to get out'
show_status(player_name, health, location, situation)