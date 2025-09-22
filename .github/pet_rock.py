print("Hello, welcome to pet rock simulator!")
print("You have the ability to care for a pet rock, make the right decisions so your pet rock lives a long, happy life! or else...")
print("*Tip: make sure to not overdo or underdo tasks.")
PetRockName = input (f"What do you name your pet rock?:")
print(f"You are now caring for your pet rock; {PetRockName}")


Hunger = 7
Happiness = 7
Cleanliness = 7

while Hunger < 10:
    decisions = input(f"Do you want to 1. feed {PetRockName} 2. play with {PetRockName} 3. clean {PetRockName} 4. do nothing, or 5. stop caring for your rock. :")


    if (decisions == '1'):
            Hunger += 1
            Happiness += 1
            Cleanliness -= 1
    if (decisions == '2'):
            Hunger -= 1
            Happiness += 1
            Cleanliness -= 1
    if (decisions == '3'):
            Hunger -=1
            Happiness +=1
            Cleanliness += 1 
    if (decisions == '4'):
            Hunger -= 1
            Happiness -= 1
            Cleanliness -= 1
            
    print("Stats:")
    print(f"Hunger = {Hunger}/10")
    print(f"Happiness = {Happiness}/10")
    print(f"Cleanliness = {Cleanliness}/10")
          
    if Hunger == 11 or Cleanliness == 11 or Happiness == 11 or Hunger == 0 or Cleanliness == 0 or Happiness == 0 or decisions == '5':
        break
if Hunger == 11:
       print(f"You let {PetRockName} get too full! Overfeeding is bad for pet rocks.{PetRockName} was taken away from you!")
if Cleanliness == 11:
       print(f"{PetRockName} got too clean. They started to become glossy, (not a good look for a pet rock owner). {PetRockName} was taken away from you!")
if Happiness == 11:
       print(f"{PetRockName} got too happy, their decision making abilities got poor. {PetRockName} got taken away from you!")
if Happiness == 0:
       print(f"{PetRockName} got too sad :(. {PetRockName} got taken away from you.")
if Hunger == 0:
       print(f"{PetRockName} is starving. Luckily PRPS (Pet Rock Protective Services) took {PetRockName} away from you just in time.")
if Cleanliness == 0:
       print(f"{PetRockName} got too dirty! Everyone noticed how smelly {PetRockName} had become, luckily someone stepped in and {PetRockName} got taken away from you!")
if decisions == '5':
       print(f"{PetRockName} is sad to see you are abandoning them :(")

