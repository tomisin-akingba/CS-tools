import string

def check_password_strength(password, common_passwords):
    score = 0
    length = len(password)

    # Check for character types
    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    # Count the number of different character types
    character_types = sum([upper_case, lower_case, special, digits])

    # Check if password is common
    if password in common_passwords:
        print("Password was found in a common list. Score = 0")
        return 0

    # Scoring based on length
    if length >= 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    # Scoring based on character types
    score += min(character_types - 1, 3)  # Max 3 points for character types

    return score

def main():
    password = "t0mi5in#is#noTnsininiwniw"

    # Load common passwords from file
    with open('common.txt', 'r') as f:
        common_passwords = f.read().splitlines()

    score = check_password_strength(password, common_passwords)

    # Provide feedback based on score
    if score < 2:
        print(f"Password is quite weak! Score: {score} / 7")
    elif score == 2:
        print(f"Password could be stronger! Score: {score} / 7")
    elif score == 3:
        print(f"Password is pretty good! Score: {score} / 7")
    elif score > 3:
        print(f"Password is very strong! Score: {score} / 7")

if __name__ == "__main__":
    main()