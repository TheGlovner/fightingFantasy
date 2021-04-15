"""
This is the main runner for the book program. On first run it will process through
the charcter creation, then begin the adventure, this will continue processing
within a loop until the player either completes the adventure or dies. At which point
they can try again.
"""
from Dice import rollDice
from CharacterCreation import createYourAdventurer
from GUIController import renderWindow
import json

project_root = "C:/programmingProjects/pythonProjects/repos/fightingFantasyWarlockOfFiretopMountain/"
json_directory = "workspace/Include/resources/jsonDirectory/"
scenario_text_directory = "workspace/Include/resources/scenarioTextDirectory/"
image_directory = "workspace/Include/resources/imageDirectory/"

##player = createYourAdventurer()
player = {"Name": "Bobby", "Strength": 6, "Skill": 6, "Luck": 6, "Status": "Alive"}
print(f'Welcome to your adventure {player["Name"]}')
print(f'Your strength score is: {player["Strength"]}')
print(f'Your skill score is: {player["Skill"]}')
print(f'Your luck score is: {player["Luck"]}')
print("Let us begin.")

with open(project_root + json_directory + "start.json") as json_file:
    scenario_controller =  json.load(json_file)

print(scenario_controller)

while player["Status"] == "Alive":

    with open(project_root + scenario_text_directory + scenario_controller["ScenarioPath"], 'r') as file:
        scenario_controller["ScenarioText"] = file.read()

    scenario_controller["ScenarioImage"] = project_root + image_directory + scenario_controller["ImagePath"]
    print(scenario_controller["ScenarioText"])
    renderWindow(scenario_controller)


