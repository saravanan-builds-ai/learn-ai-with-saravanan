from developer import Developer
import json
from dataclasses import dataclass, asdict

def save_developer_into_file(developer:Developer):
    with open("developer.txt","w",encoding="utf-8") as file:
        content=json.dumps(asdict(developer),indent=4)
        file.write(content)


def get_developer_from_file():
    with open("developer.txt","r") as file:
        return file.read()

def append_developer_into_file(developer:Developer):
    with open("developer.txt","a") as file:
        content = json.dumps(asdict(developer), indent=4)
        file.write(content)




if __name__=="__main__":
    developer = Developer(
        name="Saravanan",
        experience=13,
        skills=["Kotlin","Python","AI Engineer","Fast API"]
    )
    append_developer = Developer(
        name="Venky",
        experience=13,
        skills=["Kotlin","Python","AI Engineer","Fast API"],
    )
    save_developer_into_file(developer)
    print(get_developer_from_file())
    append_developer_into_file(append_developer)
    print(get_developer_from_file())