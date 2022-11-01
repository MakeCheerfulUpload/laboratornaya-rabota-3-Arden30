import re

phone = input("Input phone number: ")
match = re.fullmatch(r"(?:[+]\d{1,2}|\d{1,2})?(?:(\s*[\-]?[(]?)\d{3}[)]?)?(?:[\-]?\s*\d{3})(?:[\-]?\s*\d{2})(?:[\-]?\s*\d{2})", phone)
if match:
    new = match[0]
    final = re.sub(r"\D+", r"", new)
    print(final)
else:
    print("smth is wrong with your number...")