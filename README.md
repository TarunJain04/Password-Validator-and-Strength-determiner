# Password Validator & Strength Checker

A simple Python utility to validate passwords against strict rules and estimate password strength based on character diversity and complexity.

## Features

- Enforces strong password rules
- Detects invalid characters and patterns
- Checks:
  - Length (8–19 characters)
  - Minimum digits, lowercase, uppercase, special characters
  - No spaces
  - No invalid characters
  - No sequential/repeating patterns
- Generates a strength rating:
  - VERY WEAK
  - WEAK
  - MODERATE
  - STRONG
  - VERY STRONG
  - ELITE

## Password Rules

A valid password must:
- Be 8 to 19 characters long
- Contain at least 2 digits
- Contain at least 3 lowercase letters
- Contain at least 1 uppercase letter
- Contain at least 2 special characters (@#$%&*_-+!)
- Not contain spaces
- Not include invalid characters
- Avoid sequential/repeating patterns (e.g. `111`, `abc`, `aab`)

## Usage

```python
password = input("Enter your password: ")

result = checkPassword(password)

if result is True:
    confirm = input("Confirm your password: ")

    if password == confirm:
        print("Password set successfully")
        print("Strength:", strength(password))
    else:
        print("Passwords do not match!")
else:
    print(result)
```

## Strength Function

The strength score is based on:
- Character type counts
- Total length
- Unique characters
- Pattern diversity

It returns a category instead of a raw score for simplicity.

## Example

```
Enter your password: Abc@12#xY
Password set successfully
Strength: STRONG
```

## Notes

- Designed for learning and basic validation use cases
- Not intended for production-grade security systems
