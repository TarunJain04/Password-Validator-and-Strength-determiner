import re

SPECIAL_CHARS = "@#$%&*_-+!"


def checkPassword(password):
    if len(password) not in range(8, 20):
        return "password shall be a minimum of 8 and a maximum of 19 characters"

    digit, lower, upper, special = 0, 0, 0, 0

    for i in range(len(password)):
        if password[i].isdecimal():
            digit += 1
        elif password[i].islower():
            lower += 1
        elif password[i].isupper():
            upper += 1
        elif password[i] in SPECIAL_CHARS:
            special += 1
        elif password[i] == ' ':
            return "spaces are not allowed"
        else:
            return f"{password[i]} is not allowed in the password"

    if digit < 2:
        return "minimum 2 digits required"

    if lower < 3:
        return "minimum 3 lower case alphabets required"

    if upper < 1:
        return "minimum 1 upper case alphabet required"

    if special < 2:
        return "minimum 2 special characters required"

    for i in range(len(password) - 2):
        a, b, c = password[i], password[i + 1], password[i + 2]

        if a.isalnum() and b.isalnum() and c.isalnum():
            if abs(ord(b) - ord(a)) < 2 and abs(ord(c) - ord(b)) < 2:
                return "avoid sequential or repeating patterns like 111 aBc 121 aac ..."

    return True


def show_requirements():
    print("Password must satisfy:")
    print("  • Length: 8–19 characters")
    print("  • At least 2 digits")
    print("  • At least 3 lowercase letters")
    print("  • At least 1 uppercase letter")
    print("  • At least 2 special characters (@#$%&*_-+!)")
    print("  • No invalid/space characters")
    print("  • No sequential/repeating patterns (e.g. 111, abc, aab)")


def strength(password):
    digit, lower, upper, special = 0, 0, 0, 0

    total = len(password)
    distinct = len(set(password))

    for c in password:
        if c.isdecimal():
            digit += 1          # +1 each
        elif c.islower():
            lower += 2          # +2 each
        elif c.isupper():
            upper += 2          # +2 each
        elif c in SPECIAL_CHARS:
            special += 3        # +3 each

    # diversity / transition bonus
    s = [x for x in re.split(f'[{re.escape(SPECIAL_CHARS)}]+', password) if x]
    d = [x for x in re.split(r'\d+', password) if x]
    l = [x for x in re.split(r'[a-z]+', password) if x]
    u = [x for x in re.split(r'[A-Z]+', password) if x]

    diversity = len(s) + len(d) + len(l) + len(u)

    score = (
        digit +
        lower +
        upper +
        special +
        total +
        distinct +
        diversity
    )

    """
    Estimated practical score range under constraints:

    Minimum ≈ 31
    Maximum ≈ 89
    """

    if score < 40:
        return "VERY WEAK"
    elif score < 50:
        return "WEAK"
    elif score < 60:
        return "MODERATE"
    elif score < 70:
        return "STRONG"
    elif score < 80:
        return "VERY STRONG"
    else:
        return "ELITE"



password = input("Enter your password: ")

result = checkPassword(password)

if result is True:
    confirm = input("Confirm your password: ")

    if password == confirm:
        print("Password set successfully")
        print("Strength:", strength(password))
    else:
        print("Passwords do not match! Try again later")
else:
    print(result)
