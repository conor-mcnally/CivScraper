from Leaders import combined
import textdistance



keys = combined.keys()
user_input = input("Enter leader name: ")
for i in keys:
    sim = textdistance.levenshtein.normalized_similarity(i, user_input)
    if sim >= 0.75:
        user_input = i

print("\nAbility Title: \n", combined[user_input].ability_title)
print("\nAbility Text: \n", combined[user_input].ability_text)
print("\nAgenda Title: \n", combined[user_input].agenda_title)
print("\nAgenda Text: \n", combined[user_input].agenda_text)


#Yeo she works
