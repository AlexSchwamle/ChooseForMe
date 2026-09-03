import sys
from secrets import choice 
from time import sleep 

if len(sys.argv) < 3:
    print("Usage: choose option1 option2 [option3 ...]")
    sys.exit(1)

choices = sys.argv[1:]

funText = f"Flipping {len(choices)}-dimensional coin"
print(funText, end="")

for countdown in range(3, 0, -1):
    funText += "."
    print(f"\r{funText}", end="", flush=True)
    sleep(1)

flippedCoin = choice(choices)
clearRestOfTerminalLine = " " * (80-len(funText))
print(f"\rThou Shalt: {flippedCoin}{clearRestOfTerminalLine}")