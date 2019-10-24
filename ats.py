"""Convert an ascii-art text its representation in emojis,
   Suitable for copying and pasting into Slack"""

from art import *

font = "unarmed" # Uses only hash chars in output


# To generalize, do some argparsing instead of these
emoji = "hand"
blank_emoji = "black_square"  # would work better with an actually fully blank emoji
message = "HI"

def emojify(ascii_art):
    emojied = []
    emojied.append(colonify(blank_emoji))
    for each in ascii_art:
        if each == " ":
            emojied.append(colonify(blank_emoji))
        elif each in ("\n"):
            emojied.append("\n")
            emojied.append(colonify(blank_emoji)) # this will leave one extra blank at the end
        elif each in ("\r"):
            pass
        else:
            emojied.append(colonify(emoji))
    del emojied[-1] # remove the extra blank
    return "".join(emojied)


def colonify(emoji_text):
    return "".join([":", emoji_text, ":"])

def main():
    Art = text2art(message, font)
    Emojified = emojify(Art)
    print()
    print(Art)
    print()
    print(Emojified)

if __name__ == "__main__":
    main()