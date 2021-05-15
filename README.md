# Minecraft speedrunning reset macro

## Description

This is as-multiplatform-as-I-could Python reset macro for Minecraft speedrunning. Supports Windows, Linux with X11 and MacOS (tested on Big Sur). Written for Python 3.6+.

## Versions/Categories covered

Currently covered:

* 1.16 Random seed glitchess
* 1.16 Set seed glitchless
* 1.15 Random seed glitchless
* 1.14 Random seed glitchless

## Default keybinds

* `Ctrl + m` creates new RSG world, works for 1.14+
* `Ctrl + k` creates new SSG world, works only in 1.16
* `Ctrl + n` exits current singleplayer world, works for 1.14+
* `Ctrl + l` exits macro gracefully, although good old `Ctrl + c` works as well

## Installation instruction

_Since the macro is written for Python, some steps are troublesome now, might try to correctly package it later_

1. Make sure you have Python 3.6+ and PIP installed - you can grab Python from [Python's site](https://www.python.org/) or install it through your platform's package manger of choice (probably Chocolatey for Windows, Homebrew for Mac and whatever your distribution's package manager is).
2. If you have git installed and know how to use it, clone the repo to preferred destination. Otherwise, click the `Code` button on project's page and then `Download ZIP`. After that, unzip it to preferred desitnation.
3. Run `pip install -r requirements.txt` in your terminal emulator
4. _(Optional step for MacOS)_ open `Security and Privacy` and give Accessibility and Screen Recording permissions to your terminal emulator - accessibility permission is for keybinds to work, screen recording to detect wheter Minecraft is the window in focus in order not to run macro somewhere random.
5. _Optional step for MacOS) I'd recommend changing keybinds in `src/config` file, as default ctrl can be a bit wonky._
6. Run `python3 main.py` in your terminal emulator. On Linux and MacOS you need to run `sudo python3 main.py` because of inner workings of `keyboard` module.
7. _(Optional for every platform) Change `KEY_DELAY_IN_MILISECONDS` in `src/config.py` to something higher if the macro is too fast_
8. Start using macro. 🤷
