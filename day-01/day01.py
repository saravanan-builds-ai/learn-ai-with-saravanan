from datetime import date

def get_learning_update(name:str,day:int,topic:str)-> str:
    return (
        f"Learn with {name}: "
        f"Day {day} | "
        f"Learning {topic}"
    )

if __name__ == "__main__":
    print("AI Engineering Journey")
    print(f"Date: {date.today()}")
    update= get_learning_update(
        name="Saravanan",
        day=1,
        topic="Python fundamentals"
    )
    print(update)