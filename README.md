# ascii-to-slack
Convert a text message to ascii art and slack emojis

![sample output](/shake.png)

## Usage


```
$ python ats.py -m HI

Converting 'HI' to representation using :smile: emoji...

#  #  ###
#  #   #
####   #
#  #   #
#  #   #
#  #  ###



:white_small_square::smile::white_small_square::white_small_square::smile::white_small_square::white_small_square::smile::smile::smile::white_small_square::white_small_square::white_small_square:
:white_small_square::smile::white_small_square::white_small_square::smile::white_small_square::white_small_square::white_small_square::smile::white_small_square::white_small_square::white_small_square::white_small_square:
:white_small_square::smile::smile::smile::smile::white_small_square::white_small_square::white_small_square::smile::white_small_square::white_small_square::white_small_square::white_small_square:
:white_small_square::smile::white_small_square::white_small_square::smile::white_small_square::white_small_square::white_small_square::smile::white_small_square::white_small_square::white_small_square::white_small_square:
:white_small_square::smile::white_small_square::white_small_square::smile::white_small_square::white_small_square::white_small_square::smile::white_small_square::white_small_square::white_small_square::white_small_square:
:white_small_square::smile::white_small_square::white_small_square::smile::white_small_square::white_small_square::smile::smile::smile::white_small_square::white_small_square::white_small_square:
:white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square::white_small_square:
```

For additional option, use `--help` of course:

```
$ python ats.py --help
usage: ats.py [-h] [--font FONT] [-e EMOJI] [-b BLANK_EMOJI] -m MESSAGE

text to ascii art to slack

optional arguments:
  -h, --help            show this help message and exit
  --font FONT           name of art lib font to use
  -e EMOJI, --emoji EMOJI
                        emoji name
  -b BLANK_EMOJI, --blank-emoji BLANK_EMOJI
  -m MESSAGE, --message MESSAGE
                        short text message
```