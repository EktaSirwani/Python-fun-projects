# A company wants a simple tool that checks whether a password is secure.

# Requirements:

# * Ask the user to enter a password.
# * Check whether the password:

#   * Is at least 8 characters long
#   * Contains at least one number
#   * Contains at least one uppercase letter
# * Display whether the password is:

#   * Weak
#   * Moderate
#   * Strong

# * Give suggestions on how to improve the password.

def password_complexity_check():

    #take user input for password
    print("Please input the password:")
    password=input()
    if password == "":
        print("Password cannot be empty")
              
    #initializing score and dictionary for 3 flags
    score = 0
    complexity = {'length': 0, 'number': 0, 'uppercase': 0}

    #checks for scoring
    if len(password) >= 8:
        complexity.update({'length': 1})
        score += 1


    #checks for number
    if any(c.isdigit() for c in password):
        complexity.update({'number': 1})
        score += 1

    #checks for uppercase
    if any(s.isupper() for s in password):
        complexity.update({'uppercase': 1})
        score += 1

    #password verdict
    if "password" in password:
        print("Your password cannot contain password")
    if score == 0 or score == 1:
        print("Your password is weak.")
    elif score == 2:
        print("Your password is moderate.")
    elif score == 3:
        print("Hooray! Your password is strong!")

    if score < 3:
        print("You can improve your password by ensuring that your password has:")
        
        if complexity['length'] == 0:
            print("8 characters or more")

        if complexity['number'] == 0:
            print("At least one numeric character")

        if complexity['uppercase'] == 0:
            print("At least one uppercase character")
    