import Config 
import sys
from secrets import choice, randbelow
from time import sleep 

CHOICE_ANIMATION_STEP_DUR = 0.1 # seconds 
RANDCHAR_ANIMATION_STEP_DUR = 0.02 
MAGIC_HIDE_CURSOR_CODE = "\033[?25l"
MAGIC_SHOW_CURSOR_CODE = "\033[?25h"
MAGIC_CLEAR_LINE_CODE = "\033[2K"

def reprintLine(text: str):
    print(f"{MAGIC_CLEAR_LINE_CODE}\r{text}", end="", flush=True)
def hideTerminalCursor():
    print(MAGIC_HIDE_CURSOR_CODE, end="", flush=True)
def showTerminalCursor():
    print(MAGIC_SHOW_CURSOR_CODE, end="", flush=True)

def getRandomText(choices: list[str]|str) -> str:
    return choice(choices)

def getFunTextBase(choices: list[str]) -> str:
    return Config.funTextBase % len(choices)
def getFinalChoiceText(choice: str) -> str:
    return Config.finalChoiceText % choice 

def playChoiceAnimation(choices: list[str]) -> None:
    for _ in range(0, int(Config.ANIMATION_DURATION / CHOICE_ANIMATION_STEP_DUR)):
        funText = getFunTextBase(choices) + getRandomText(choices)
        reprintLine(funText)
        sleep(CHOICE_ANIMATION_STEP_DUR)

def playRandomCharacterAnimation(choices: list[str]) -> None:
    animationSteps = int(Config.ANIMATION_DURATION / RANDCHAR_ANIMATION_STEP_DUR)
    largestChoiceLength = max(len(choice) for choice in choices)
    numberOfCharactersToShow = max(randbelow(largestChoiceLength+1), 5) # always animate at least 5 characters
    stepsPerCharacter = animationSteps // numberOfCharactersToShow
    curNumCharactersToShow = 1 
    for step in range(0, animationSteps):
        if step % stepsPerCharacter == 0:
            curNumCharactersToShow += 1

        funTextAnimationChars = "".join(getRandomText(Config.RANDOM_LETTERS) for _ in range(curNumCharactersToShow))
        funText = getFunTextBase(choices) + funTextAnimationChars
        reprintLine(funText)
        sleep(RANDCHAR_ANIMATION_STEP_DUR)

def run():
    choices = sys.argv[1:]
    print(getFunTextBase(choices), end="")

    hideTerminalCursor() # Hide blinking terminal cursor while animation plays 

    if Config.ANIMATION_TYPE == "random":
        playRandomCharacterAnimation(choices)
    elif Config.ANIMATION_TYPE == "choice": 
        playChoiceAnimation(choices)
    elif Config.ANIMATION_TYPE != "none":
        print(f"{MAGIC_CLEAR_LINE_CODE}\rYou didn't set Config.ANIMATION_TYPE to a valid value. Choosing for you...")
        roulette = choice((playRandomCharacterAnimation, playChoiceAnimation))
        roulette(choices)

    flippedCoin = getRandomText(choices)
    finalText = getFinalChoiceText(flippedCoin)
    reprintLine(finalText)

    showTerminalCursor() # Always clean up after yourself

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: choose option1 option2 [option3 ...]")
        sys.exit(1)

    run()