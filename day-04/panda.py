import pandas as pd


def simple_func(developer: dict):
    df = pd.DataFrame(developer)
    print(df)
    # Select single column
    print(df["experience"])
    # Select multiple column
    print(df[["name", "experience"]])
    # Select single row
    print(df.iloc[0])
    # Select first two row
    print(df.head(2))
    # Select last two row
    print(df.tail(2))


def filter_developer(developer: dict):
    df = pd.DataFrame(developer)
    experienced_developers = df[
        df["experience"] > 5
        ]
    experienced_developers = experienced_developers.sort_values(
        by="salary",
        ascending=False
    )
    print(experienced_developers.loc[:, ["name", "experience", "salary"]])


def save_to_csv(developer: dict):
    df = pd.DataFrame(developer)
    df.to_csv("developer.csv", index=False)


def get_from_csv():
    df = pd.read_csv(
        "developer.csv",
    )
    print(df)

def save_to_json(developer: dict):
    df = pd.DataFrame(developer)
    json=df.to_json("developer.json",orient="records",indent=4)
    print(json)

def read_json():
    df = pd.read_json(
        "developer.json"
    )
    print(df)
if __name__ == "__main__":
    developers = {
        "name": ["Arun", "Priya", "Kumar", "Divya"],
        "experience": [5, 8, 3, 10],
        "skills": ["Kotlin", "Python", "Java", "Kotlin"],
        "salary": [80000, 120000, 60000, 150000]
    }
    # simple_func(developers)
    # filter_developer(developers)
    # save_to_csv(developers)
    # get_from_csv()
    save_to_json(developers)
    read_json()