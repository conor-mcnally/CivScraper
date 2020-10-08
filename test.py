from Leaders import combined
import textdistance



keys = combined.keys()
user_input = input("Enter leader name: ")

sim = textdistance.levenshtein.similarity('test', 'text')

for i in keys:
    sim = textdistance.levenshtein.similarity(user_input, i)
    if sim <= len(i):
        user_input = i
return user_input
#use normalised similarity
#if normalised similarity is > 0.95
#input == i 

#if input <= total number of characters in len(i) for i in keys
    #return matching key, use as input

# print("\nAbility Title: \n", combined[user_input].ability_title)
# print("\nAbility Text: \n", combined[user_input].ability_text)
# print("\nAgenda Title: \n", combined[user_input].agenda_title)
# print("\nAgenda Text: \n", combined[user_input].agenda_text)
