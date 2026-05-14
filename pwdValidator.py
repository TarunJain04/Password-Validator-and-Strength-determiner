import re
import math
SPECIAL_CHARS = "@#$%&*_-+!"
MIN_LENGTH=8
MAX_LENGTH=19
def checkPassword(password):
    if len(password) not in range(MIN_LENGTH, MAX_LENGTH+1):
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
    return True
def show_requirements():
    print("Password must satisfy:")
    print("  • Length: 8–19 characters")
    print("  • At least 2 digits")
    print("  • At least 3 lowercase letters")
    print("  • At least 1 uppercase letter")
    print("  • At least 2 special characters (@#$%&*_-+!)")
    print("  • No invalid/space characters")
    print("  • Avoid sequential/repeating patterns (e.g. 111, abc, aab)")
def status(metric):
    if metric < 0.25:
        return "VERY WEAK"
    elif metric < 0.4:
        return "WEAK"
    elif metric < 0.6:
        return "MODERATE"
    elif metric < 0.75:
        return "GOOD"
    elif metric < 0.80:
        return "STRONG"
    elif metric < 0.95:
        return "VERY STRONG"
    else:
        return "ELITE"
def strength(password):
    MAX_STRENGTH=MAX_LENGTH*3
    score=0
    digits=re.findall(r"\d",password)
    lower=re.findall(r"[a-z]",password)
    upper=re.findall(r"[A-Z]",password)
    special=re.findall(f'[{re.escape(SPECIAL_CHARS)}]',password)
    
    d=len(digits)
    l=len(lower)
    u=len(upper)
    s=len(special)
    D=len(set(digits))
    L=len(set(lower))
    U=len(set(upper))
    S=len(set(special))
    
    for i in range(len(password) - 2):
        a, b, c = password[i], password[i + 1], password[i + 2]
        tri=(a+b+c)
        if tri.isalnum():
            a,b,c=tri.lower()
            if abs(ord(b) - ord(a)) < 2 and abs(ord(c) - ord(b)) < 2:
                if c.isdecimal(): D*=.9
                elif c.islower(): L*=.9
                else: U*=.9
        elif a==b and b==c:
                S*=.9

    sd=(d-D)*(D/(d+1))*.5+D*1
    sl=(l-L)*(L/(l+1))*1+L*2
    su=(u-U)*(U/(u+1))*1+U*2
    ss=(s-S)*(S/(s+1))*1.5+S*3
    
    # diversity
    _d = len(set([x for x in re.split(r'\d+', password) if x]))
    _l = len(set([x for x in re.split(r'[a-z]+', password) if x]))
    _u = len(set([x for x in re.split(r'[A-Z]+', password) if x]))
    _s = len(set([x for x in re.split(f'[{re.escape(SPECIAL_CHARS)}]+', password) if x]))
    sd+=sd*(_d/(d+1))
    sl+=sl*(_l/(l+1))
    su+=su*(_u/(u+1))
    ss+=ss*(_s/(s+1))


    score+=(sd+sl+su+ss)/MAX_STRENGTH
    
    # entropy
    N=0
    if d>0: N+=10
    if l>0: N+=26
    if u>0: N+=26
    if s>0: N+=len(SPECIAL_CHARS)
    e=len(set(password))*math.log2(N)
    E=MAX_LENGTH*math.log2(10+26+26+len(SPECIAL_CHARS))
    entropy=e/E
    return .6*score+.4*entropy*entropy
password = input("Enter your password: ")
result = checkPassword(password)
if result is True:
    confirm = input("Confirm your password: ")
    if password == confirm:
        print("Password set successfully")
        print("Strength:", status(strength(password)))
    else:
        print("Passwords do not match! Try again later")
else:
    print(result)
