name = "Saravanan"
experience = 7
current_focus = "AI Engineering"
is_learning = True
hours_per_day = 2

skills = ["Kotlin", "Python", "Jetpack Compose", "AI","Fast Api","Prompt Engineering"]

developer = {
    "name": name,
    "experience": experience,
    "focus": current_focus,
    "skills": skills,
    "location":"Dubai"
}

if experience >= 10:
    experience_level = "Senior"
elif experience >= 5:
    experience_level = "Mid-Level"
else:
    experience_level = "Junior"

print("=== Developer Profile ===")
print(f"Name: {developer["name"]}")
print(f"Experience: {developer["experience"]} years")
print(f"Level: {experience_level}")
print(f"Current Focus: {developer['focus']}")
print(f"Learning AI: {is_learning}")
print(f"Skills: {','.join(developer['skills'])}")
print(f"Number of skills: {len(developer['skills'])}")
print(f"Location: {developer['location']}")
print(f"Hours per day: {hours_per_day}")

list_skills = ["Kotlin","Jetpack Compose","AI","Fast Api","Prompt Engineering","Kotlin"]
set_skills = set(list_skills)

print(f"List skills length: {len(list_skills)}")
print(f"Set skills length: {len(set_skills)}")
