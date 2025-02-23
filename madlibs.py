# This is a simple python script to mimic the mad libs game. 
# Madlibs using string concatenation is used in the script. 
print("This is a mad libs game. The topic is - 'The Exciting Cricket Match'. Please input the data based on something related to cricket.")

print("Please give the inputs based on the prompts")
adj1 = input("Adjective: ")
fav_team_name = input("Favourite Team Name: ")
opp_team_name = input("(opposing Team Name): ")
adj2 = input("Adjective: ")
plural_noun = input("Some Plural Noun: ")
adj3 = input("Adjective: ")
adj4 = input("Adjective: ")
per_name = input("Person's name: ")
fld_pos = input("Some Fielding Position: ")
num1 = input("Some Number: ")
num2 = input("Some Number:")
fav_ckt_name = input("Favorite cricketer's name: ")
vrb1 = input("Some verb in past tense: ")
num3 = input("Some Number: ")
vrb2 = input("Some verb in past tense: ")
vrb3 = input("Some verb in past tense: ")
adj5 = input("Adjective: ")

madlib_txt = f"""It was a {adj1} day at the stadium as the {fav_team_name} faced off against {opp_team_name}. The crowd was {adj2}, cheering loudly for their favorite {plural_noun}.\
The first batsman walked onto the field, holding a {adj3} bat. The bowler ran in and delivered a {adj4} ball.\
{per_name} swung the bat and hit it straight to the {fld_pos} for a {num1}-run shot! The game was intense, and the {fav_team_name} needs {num2} runs in the last over.\
The final ball was bowled, and {fav_ckt_name} {vrb1} it for a {num3}! The crowd {vrb2} in excitement, and the team {vrb3} with joy.\
It was truly a {adj5} match to remember!"""
# Final generated text
print(madlib_txt)