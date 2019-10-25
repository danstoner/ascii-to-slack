"""Convert an ascii-art text its representation in emojis,
   Suitable for copying and pasting into Slack"""

from art import *
import argparse

def emojify(ascii_art, emoji, blank_emoji):
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
    parser = argparse.ArgumentParser(description='text to ascii art to slack')
    # '5x7' is a tall skinny font that only uses hashtags in output
    parser.add_argument("--font", default='5x7', help='name of art lib font to use')
    parser.add_argument("-e", "--emoji", default='smile', help='emoji name')
    # a completely blank emoji would work best, but this is an ok substitute in the efault emoji pack
    parser.add_argument("-b", "--blank-emoji", default='white_small_square')
    parser.add_argument("-m", "--message", required=True, help='short text message')
    args=parser.parse_args()
    print()
    print(f"Converting '{args.message}' to representation using {colonify(args.emoji)} emoji...")

    Art = text2art(args.message, args.font)
    Emojified = emojify(Art, args.emoji, args.blank_emoji)
    print()
    print(Art)
    print()
    print(Emojified)

if __name__ == "__main__":
    main()