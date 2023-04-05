# Franchesca Marie Donadillo
# BSCPE 1-5
# ASSIGNMENT 2_Problem 2 - Decryption

from rich.console import Console
from rich.theme import Theme
from rich import print

design = Theme({"title": "bold magenta", "decrypt": "underline bold yellow", "blinky": "bold green blink"})
console = Console(theme = design)

title = "Problem_2 - Decryption"
new_title = title.center(55).upper()
console.print("\n" + new_title + "\n", style = "title")

# ask user input
user_input = input("Enter some characters: ")
output = ""

# loop all throughout the user input
for i in range(len(user_input)):
    # change * into a
    if user_input[i] == "*":
        output += "a"
    # change & into e
    elif user_input[i] == "&":
        output += "e"
    # change # into i
    elif user_input[i] == "#":
        output += "i"
    # change + into o
    elif user_input[i] == "+":
        output += "o"
    # change ! into u
    elif user_input[i] == "!":
        output += "u"
    else:
        output += user_input[i]

star = "*"*60
starla = star.center(65)

# print the decrypted text of the user
console.print("\n" + f"[bold green]{starla}[/bold green]" + "\n\nThe decrypted text is ", end = "")
console.print(output, style = "decrypt")
console.print("\n" + starla, style = "blinky")
