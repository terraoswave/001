# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define s = Character("Saintess") # narasi dengan nama karakter
define b = Character("") # narasi tanpa nama

# Resize transform
transform resize:
    zoom 0.4  # mengatur ukuran

# The game starts here.
label start:

    scene village

    # Show character using corrected transform syntax
    

    b "This is the story of a young girl who wants to become a saintess."

    b "She doesn't have any skills or devotion. She just thinks being a saintess is cool."
    
    show saintess at right, resize
    with fade # fade itu semuanya satu layar cuk

    s "Today's prayer is done. I need to do more work for the village."

    s "I need to wash the clothes, "

    s "Congratulations."

    return
