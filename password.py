import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Initialize strength score and feedback list
    score = 0
    feedback = []

    # Check each criterion and provide feedback
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if digit_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, etc.).")

    # Determine password strength level based on the score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Output result
    return strength, feedback

# User input
password = input("Enter a password to assess its strength: ")

# Assess password strength and print feedback
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
for advice in feedback:
    print("- " + advice)
