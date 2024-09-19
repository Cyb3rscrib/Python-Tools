### Password Brute-Forcer - README

---

## Overview

This Python script performs a **password brute-force attack** on a login page to find the correct password for a specified username. It reads a list of potential passwords from a file, sends HTTP GET requests to a login page with each password, and checks for a successful login based on a predefined success message.

**WARNING**: This script should only be used for educational purposes or on systems where you have explicit permission to perform testing. Unauthorized access or brute-forcing is illegal and unethical.

---

## Features

- Reads a list of potential passwords from a file (`passwords.txt`).
- Sends HTTP GET requests to a login page with the username and each password.
- Checks the response for a specific success message to determine if the login was successful.
- Prints the correct password when found and stops further attempts.

---

## Prerequisites

1. **Python 3.x** installed on your machine.
2. **`requests`** library installed:
   - Install it via pip if not already installed:
     ```bash
     pip install requests
     ```

---

## Usage Instructions

1. **Prepare Password List**:
   - Create a file named `passwords.txt` in the same directory as the script.
   - Add potential passwords to this file, separated by commas. For example:
     ```
     password123,admin123,qwerty,letmein,123456
     ```

2. **Update the Script**:
   - Ensure the `url` variable points to the correct login page. By default, it is set to `http://127.0.0.1/login.php` for local testing.

3. **Run the Script**:
   - Execute the script using Python:
     ```bash
     python password_bruteforce.py
     ```

4. **Script Output**:
   - The script will print the correct password if found. If no correct password is found, it will complete without printing anything.

---

## Code Structure

### 1. **Reading Potential Passwords**:
```python
with open("passwords.txt", "r") as file:
    passwords = file.read().split(",")
```
- This block reads the `passwords.txt` file and splits the content into a list of passwords.

### 2. **Brute-Forcing Login**:
```python
for password in passwords:
    response = requests.get(url, params={"user":"admin", "pass": password})
```
- For each password in the list, the script sends a GET request to the login page with the username set to `"admin"` and the current password.

### 3. **Checking for Success**:
```python
if "Welcome admin" in response.text:
    print("Correct password found:", password)
    break
```
- The script checks if the response text contains `"Welcome admin"`, which indicates a successful login.
- If found, it prints the correct password and stops further attempts.

### 4. **Optional Logging**:
```python
# else:
#     print("Incorrect password:", password)
```
- This section is commented out but can be uncommented to print incorrect password attempts for debugging purposes.

---

## Important Notes

- **Ethics & Legality**: This script performs a brute-force attack and should only be used in environments where you have explicit permission to test. Unauthorized use is illegal and unethical.
- **HTTP Method**: The script uses HTTP GET requests to test passwords. Many login systems use POST requests for authentication, which would require modifying the script to handle form submissions.

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This tool is provided for educational purposes only. The use of this script to compromise systems without permission is illegal. The developer is not responsible for any misuse or damage caused by this script.

---

## Future Improvements

1. **Error Handling**: Add error handling for network issues or invalid responses.
2. **POST Request Support**: Modify the script to support POST requests if the login page uses them.
3. **Rate Limiting**: Implement delays between requests to avoid triggering rate-limiting mechanisms.

---

This script provides a basic approach to brute-forcing passwords but always ensure compliance with legal and ethical guidelines when using it.
