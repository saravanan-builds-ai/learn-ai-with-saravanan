from developer import Developer
def analyze_developer(developer: Developer):
    print("Developer:", developer)
    print(f"Experience: {developer.experience} years")

    unique_skills=set(developer.skills)
    print(f"Total unique skills: {len(unique_skills)}")

    if developer.experience>=10:
        print("Level: Senior Developer")
    elif developer.experience>=5:
        print("Level: Mid-Level Developer")
    else:
        print("Level: Junior Developer")