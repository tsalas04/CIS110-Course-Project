print(f"Hello there! You are about to be part of choosing the light or dark! ")
print(f"Part of the fun is you get to change the character to your liking.")
print(f"After each answer you will have to hit the enter key to move on.")
input(f"\nPress the enter key to continue...")

species = input("\nWhat species is your character:  ")
characterName = input("What is your characters name?  ")
planetName = input("Which planet are you on?  ")
movie = input("What is your favorite movie?  ")
food = input("What is your favorite food?  ")

print(f"\nMay the Force be with you!")
print(f"\nThere once was a strong {species} named {characterName}. ")
print(f"\n{characterName} Could not wait to explore {planetName}.  ")
print(f"\n{characterName} Recieved bad new of a fallen Jedi and has to head to {planetName}.  ")
print(f"\n{characterName} Rushed to the space port to pick {movie} to watch and {food} to eat on the flight.  ")
print(f"\nAs you find your fallen brother in arms on planet Saturn you are attacked by an enemy wielding a red saber called a sith!  ")

defendYourself = input(f"\nShould {characterNAme} defend yourself? Type yes or no:  ")
if defendYourself == "yes":
    print(f"\n{characterNAme} in a rage you defend yourself and disarms the enemy sith by cutting his hand off.  ")
    print(f"\nThe sith now on his knees screams out that he surrenders and has no weapon.  ")
    print(f"\nLooking at your fallen brother left to waste away by the elements you have to make a tough decision.  ")
else:
    print(f"\n{characterName} uses the force to focus and  disarms the sith by using a force push.  ")
    print(f"\nThe sith now on his back with no saber in hand yells out youre lucky you disarmed me.  ")
    print(f"\nLooking at your fallen brother left to waste away by the elements you have to make a tough decision.  ")

    