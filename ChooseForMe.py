import Config 
import sys
from secrets import choice, randbelow
from time import sleep 

CHOICE_ANIMATION_STEP_DUR = 0.1 # seconds 
RANDCHAR_ANIMATION_STEP_DUR = 0.02 
MAGIC_HIDE_CURSOR_CODE = "\033[?25l"
MAGIC_SHOW_CURSOR_CODE = "\033[?25h"
RANDOM_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?#"


def hideTerminalCursor():
    print(MAGIC_HIDE_CURSOR_CODE, end="", flush=True)
def showTerminalCursor():
    print(MAGIC_SHOW_CURSOR_CODE, end="", flush=True)

def getRandomText(choices: list[str]|str) -> str:
    return choice(choices)

def playChoiceAnimation(funTextBase: str, clearRestOfTerminalLine: str,choices: list[str]) -> None:
    for _ in range(0, int(Config.ANIMATION_DURATION / CHOICE_ANIMATION_STEP_DUR)):
        funText = funTextBase + getRandomText(choices)
        print(f"\r{funText}{clearRestOfTerminalLine}", end="", flush=True)
        sleep(CHOICE_ANIMATION_STEP_DUR)

def playRandomCharacterAnimation(funTextBase: str, clearRestOfTerminalLine: str, choices: list[str]) -> None:
    animationSteps = int(Config.ANIMATION_DURATION / RANDCHAR_ANIMATION_STEP_DUR)
    largestChoiceLength = max(len(choice) for choice in choices)
    numberOfCharactersToShow = max(randbelow(largestChoiceLength+1), 5) # always animate at least 5 characters
    stepsPerCharacter = animationSteps // numberOfCharactersToShow
    curNumCharactersToShow = 1 
    for step in range(0, animationSteps):
        if step % stepsPerCharacter == 0:
            curNumCharactersToShow += 1
        
        funText = funTextBase + "".join(getRandomText(RANDOM_LETTERS) for _ in range(curNumCharactersToShow))
        print(f"\r{funText}{clearRestOfTerminalLine}", end="", flush=True)
        sleep(RANDCHAR_ANIMATION_STEP_DUR)

def run():
    choices = sys.argv[1:]
    funTextBase = f"Flipping {len(choices)}-dimensional coin: "
    print(funTextBase, end="")
    
    largestChoiceLength = max(len(choice) for choice in choices)
    clearRestOfTerminalLine = " " * (80-len(funTextBase)-largestChoiceLength) 

    hideTerminalCursor() # Hide blinking terminal cursor while animation plays 

    if Config.ANIMATION_TYPE == "random":
        playRandomCharacterAnimation(funTextBase, clearRestOfTerminalLine, choices)
    elif Config.ANIMATION_TYPE == "choice": 
        playChoiceAnimation(funTextBase, clearRestOfTerminalLine, choices)
    elif Config.ANIMATION_TYPE != "none":
        print("You didn't set Config.ANIMATION_TYPE to a valid value. Choosing for you...")
        roulette = choice((playRandomCharacterAnimation, playChoiceAnimation))
        roulette(funTextBase, clearRestOfTerminalLine, choices)

    flippedCoin = getRandomText(choices)
    print(f"\rThou Shalt: {flippedCoin}{clearRestOfTerminalLine}")

    showTerminalCursor() # Always clean up after yourself

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: choose option1 option2 [option3 ...]")
        sys.exit(1)

    run()