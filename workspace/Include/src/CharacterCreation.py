"""
Controls the character creation process at the start of the adventure.
"""

from Dice import rollDice


def createYourAdventurer():
  character = {"Name": "", "Strength": 0, "Skill": 0, "Luck": 0, "Status": "Alive"}

  character["Name"] = input("What is your name brave adventurer?\n")
  
  print(
"""
Now you must find out how well you have trained. 

1 is the lowest and 6 is the highest.

You are allowed a maximum of three dice rolls for each attribute.
"""
  )

  print("First we shall test your strength!")
  character["Strength"] = attributeCreation("strength")

  print("Second, your skill!")
  character["Skill"] = attributeCreation("skill")

  print("Finally, your luck!")
  character["Luck"] = attributeCreation("luck")

  return character


"""
The function below controls the dice rolls for the selected attribute.
"""
def attributeCreation(attribute):
  loopHalt = False
  rolls = 0
  maxRolls = 3
  diceRoll = 0

  input("Press Enter to roll the dice.")
  while rolls < maxRolls and loopHalt == False:
    rolls = rolls + 1
    diceRoll = rollDice()
    if rolls < maxRolls:
      accept = str.lower(input(
f"""
Your {attribute} score is {diceRoll}. 

If you want to accept this dice roll enter 'Y'.
If you want to roll again (you have {maxRolls - rolls} rolls left) enter 'N'.




"""
      ))
    else:
      print(
            f"""
Your {attribute} score is {diceRoll}. 

You have no rolls left.




            """
      )
      loopHalt = True

    if accept == "y":
      loopHalt = True

  return diceRoll

