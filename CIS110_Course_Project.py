print(f"Hello there! You are about to be part of choosing the light or dark! ")
print(f"Part of the fun is you get to change the character to your liking.")
print(f"After each answer you will have to hit the enter key to move on.")
input(f"\nPress the enter key to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    #5 Questions before the story begins
    species = input(f"\nWhat species is your character:  ")
    while (len(species) == 0):
        species = input(f"Please enter a species:  ")
        
    characterName = input(f"What is your characters name?  ")
    while (len(characterName) == 0):
        characterName = input(f"Please enter a character name:  ")
        
    planetName = input(f"Which planet do you wish you could explore?  ")
    while (len(planetName) == 0):
        planetName = input(f"Please enter a planet name:  ")
        
    movie = input(f"What is your favorite movie?  ")
    while (len(movie) == 0):
        movie = input(f"Please enter your favorite movie name:  ")
        
    food = input(f"What is your favorite food?  ")
    while (len(food) == 0):
        food = input(f"Please enter your favorite food:  ")
        
    #Story Starts
    print(f"\nMay the Force be with you!")
    print(f"\nThere once was a strong {species} named {characterName}. ")
    print(f"\n{characterName} Could not wait to explore {planetName}.  ")
    print(f"\n{characterName} Recieved bad news of a fallen Jedi and has to head to {planetName}.  ")
    print(f"\n{characterName} Rushed to the space port to pick {movie} to watch and {food} to eat on the flight.  ")
    print(f"\nAs you find your fallen brother in arms on {planetName} you are attacked by an enemy wielding a red saber called a sith!  ")

    #Decision 1
    defendYourself = input(f"\nShould {characterName} defend himself? Type yes or no:  ")
    while defendYourself.lower() != "yes" and defendYourself.lower() != "no":
        defendYourself = input("Please type yes or no:  ")
    
    if defendYourself == "yes":
        print(f"\n{characterName} In a rage you defends himself and disarms the enemy sith by cutting his hand off.  ")
        print(f"The sith now on his knees screams out that he surrenders and has no weapon.  ")
        print(f"Looking at your fallen brother left to waste away by the elements you have to make a tough decision.  ")
    else:
        print(f"\n{characterName} Uses the force to focus and disarms the sith by using a force push.  ")
        print(f"The sith now on his back with no saber in hand yells out youre lucky you disarmed me.  ")
        print(f"Looking at your fallen brother left to waste away by the elements you have to make a tough decision.  ")
    
    print(f"Struggling to breath on {planetName} {characterName} Trys to calm down to focus on wether to strike the dangerous enemy down while he is on his knees or risk trying to arrest him.  ")
    print(f"Remembering all the tough decisions made on {movie} he makes his decision.  ")

    #Decision 2
    strikeDown = input(f"\nShould {characterName} strike down the defenseless sith? Type yes or no:  ")
    while strikeDown.lower() != "yes" and strikeDown.lower() != "no":
        strikeDown = input(f"Please type yes or no:  ")
  
    if strikeDown == "yes":
        print(f"\n{characterName} Strikes out of fear of the sith ambushing him and lets his emotions take control.  ")
        print(f"\n{characterName} Becomes overwhelmed by his emotions of loss, fear, and anger starts to scream at the top of his lungs.  ")
        print(f"No longer feeling {species} {characterName} realizes he has become the very thing he came to destroy a sith and goes into exile.  ")
    else:
        print(f"\n{characterName} Slows his breathing down to focus on his breathing so he can meditate for a brief momment.  ")
        print(f"\n{characterName} Begins to you use the force to hold down the screaming sith to arrest him.  ")
        print(f"\nFeeling {species} {characterName} trys to comfort the raging sith and leaves {planetName} realizing he has now become a master by defeating the enemy without killing.  ")
    
    #Alternate Endings
    if defendYourself == "yes" and strikeDown == "yes":
        print(f"\nAfter letting his emotions take control in all his decisions {characterName} takes the enemies weapon and continues down the same dark path of hunting what once were his brothers.  ")
        print(f"\nNo longer feeling {species} {characterName} take the bloody mask off of his fallen enemy and wears it to cover his identity.  ")
    elif defendYourself == "no" and strikeDown== "no":
        print(f"\n After fully controlling your emotions {characterName} feels connected to {planetName} and is at peace.  ")
        print(f"\Feeling connected as a {species} {characterName} heads back home to be welcomed to become a master and be on the high council.  ")
    else:
        print(f"\n{characterName} has a new love for {planetName} and decides to make a home there.  ")
        print(f"\n{characterName} now making a home decided to open a movie theater showing on {movie} movies and serves {food} food.  ")
    print("\nThe End")

    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")
            