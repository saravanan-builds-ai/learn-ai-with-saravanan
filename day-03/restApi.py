from os import name

import requests

def get_github_user(username: str):
    url = f"https://api.github.com/users/{username}"
    try:
        response= requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)
    except requests.exceptions.ConnectionError as err:
        print("Connection Error:", err)
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
    except requests.exceptions.RequestException as err:
        print("Other Error:", err)
    return None



if __name__ == "__main__":
    while True:
        inputName=input("Enter a GitHub username: ")
        if inputName == "exit":
            break
        user = get_github_user(inputName)
        if user is not None:
            print("User:", user["login"])
            print("Repo:", user["public_repos"])




