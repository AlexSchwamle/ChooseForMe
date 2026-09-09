ANIMATION_DURATION = 2.5 # Seconds it takes to run the animation below before seeing the result.
ANIMATION_TYPE = "random" # "random" = random characters, "choice" = cycle through all your choices. "none" to disable.

# These are the letters the "random" animation will randomly choose from. 
# For example, "01" would make it look like a random binary sequence of only 1s and 0s.
RANDOM_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?#" 

# The text that is printed before the final selection is printed. The %d is replaced with the number of choices you give.
funTextBase = "Flipping %d-dimensional coin: "
# The final text printed with the random choice afterwards. Can move %s if you want to have text after your choice.
finalChoiceText = "Thou Shalt: %s"