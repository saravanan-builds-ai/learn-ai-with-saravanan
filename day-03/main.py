from developer import Developer
from analyzer import analyze_developer

def main():
    developer: Developer = Developer(
        name="Saravanan",
        experience=13,
        skills=[]
    )
    developer.add_skill("Kotlin")
    developer.add_skill("Python")
    developer.add_skill("FastAPI")

    analyze_developer(developer)

if __name__ == "__main__":
    main()