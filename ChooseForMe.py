import sys
from secrets import choice 

if len(sys.argv) < 3:
    print("Usage: choose option1 option2 [option3 ...]")
    sys.exit(1)

choices = sys.argv[1:]
flippedCoin = choice(choices)
print(f"Thou Shalt: {flippedCoin}")
