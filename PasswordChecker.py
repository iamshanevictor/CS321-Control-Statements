import re

def password_checker():
    difficulty = input("Select a difficulty level (Easy, Medium, Hard): ")

    password = input("Enter a password: ")

    requirements = {
        "Easy": {"length": 6},
        "Medium": {"length": 8, "upper": True, "lower": True, "digit": True},
        "Hard": {"length": 8, "upper": True, "lower": True, "digit": True, "special": True}
    }

    req = requirements[difficulty]

    if len(password) < req["length"]:
        return f"Password must be at least {req['length']} characters long"

    if req.get("upper") and not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"

    if req.get("lower") and not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter"

    if req.get("digit") and not re.search(r"\d", password):
        return "Password must contain at least one digit"
    
    if req.get("special") and not re.search(r"\W", password):
        return "Password must contain at least one special character"

    return "Password meets all requirements"

print(password_checker())