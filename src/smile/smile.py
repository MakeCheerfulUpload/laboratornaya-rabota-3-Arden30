import re

isu = 367058
eye = [":", ";", "X", "8", "="]
nose = ["-", "<", "-{", "<{"]
mouth = ["(", ")", "O", "|", "\\", "/", "P"]
smile = fr"{eye[isu % 6] + nose[isu % 4] + mouth[isu % 7]}"
print("Your smile is:", smile)

text = input("Input your text: ")
match = re.findall(smile, text)
print("I found", len(match), "smiles")
