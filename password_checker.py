def check_password_strength(password):
    conditions_met = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        conditions_met += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letter
    if any(char.isupper() for char in password):
        conditions_met += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letter
    if any(char.islower() for char in password):
        conditions_met += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for number
    if any(char.isdigit() for char in password):
        conditions_met += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special character
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"
    if any(char in special_characters for char in password):
        conditions_met += 1
    else:
        feedback.append("Add at least one special character.")

    # Determine strength
    if conditions_met <= 2:
        strength = "Weak"
    elif conditions_met <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


def main():
    print("Password Strength Checker")
    print("--------------------------")

    password = input("Enter a password to check: ")

    strength, feedback = check_password_strength(password)

    print(f"\nPassword strength: {strength}")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password meets all recommended security criteria.")


if __name__ == "__main__":
    main()
