import sys
from secrets import choice
from time import sleep 

MAGIC_HIDE_CURSOR_CODE = "\033[?25l"
MAGIC_SHOW_CURSOR_CODE = "\033[?25h"

def hideTerminalCursor():
    print(MAGIC_HIDE_CURSOR_CODE, end="", flush=True)
def showTerminalCursor():
    print(MAGIC_SHOW_CURSOR_CODE, end="", flush=True)

def getRandomText(choices: list[str]) -> str:
    return choice(choices)

def run():
    choices = sys.argv[1:]
    funTextBase = f"Flipping {len(choices)}-dimensional coin: "
    print(funTextBase, end="")
    
    largestChoiceLength = max(len(choice) for choice in choices)
    clearRestOfTerminalLine = " " * (80-len(funTextBase)-largestChoiceLength) 

    hideTerminalCursor() # Hide cursor while animation plays 

    for _countdown in range(0, 30):
        funText = funTextBase + getRandomText(choices)
        print(f"\r{funText}{clearRestOfTerminalLine}", end="", flush=True)
        sleep(0.1)

    flippedCoin = getRandomText(choices)
    print(f"\rThou Shalt: {flippedCoin}{clearRestOfTerminalLine}")

    showTerminalCursor() # Always clean up after yourself

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: choose option1 option2 [option3 ...]")
        sys.exit(1)

    run()