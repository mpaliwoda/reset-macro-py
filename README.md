# Minecraft speedrunning reset macro

## Description

This is as-multiplatform-as-I-could-make-it Python reset macro for Minecraft speedrunning.Should fully support Windows, Linux with X11 (tested on elementaryOS Hera) and MacOS (tested on Big Sur). Could work on Wayland, but I din't even test it - see additional steps to give it a try. Written for Python 3.6+.

## Versions/Categories covered

Currently covered:

* 1.16 Random seed glitchess
* 1.16 Set seed glitchless
* 1.15 Random seed glitchless
* 1.14 Random seed glitchless

## Default keybinds for Windows

* `Ctrl + m` creates new RSG world, works for 1.14+
* `Ctrl + k` creates new SSG world, works only in 1.16
* `Ctrl + n` exits current singleplayer world, works for 1.14+
* `Ctrl + l` exits macro gracefully, although good old `Ctrl + c` works as well

## Default keybinds for Linux

* `Ctrl + m` creates new RSG world, works for 1.14+
* `Ctrl + k` creates new SSG world, works only in 1.16
* `Ctrl + n` exits current singleplayer world, works for 1.14+
* `Ctrl + l` exits macro gracefully, although good old `Ctrl + c` works as well

## Default keybinds for MacOS

* `Cmd + u` creates new RSG world, works for 1.14+
* `Cmd + k` creates new SSG world, works only in 1.16
* `Cmd + n` exits current singleplayer world, works for 1.14+
* `Cmd + l` exits macro gracefully, although good old `Ctrl + c` works as well

## Installation instruction

_Since the macro is written for Python, some steps are troublesome now, might try to correctly package it later_.

1. Make sure you have Python 3.6+ and PIP installed - you can grab Python from [Python's site](https://www.python.org/) or install it through your platform's package manger of choice (probably Chocolatey for Windows, Homebrew for Mac and whatever your distribution's package manager is on Linux).
2. If you have git installed and know how to use it, clone the repo to preferred destination. Otherwise, click the `Code` button on project's page and then `Download ZIP`. After that, unzip it to preferred desitnation.
3. Run `pip install -r requirements.txt` in your terminal emulator
4. _(Additional step for MacOS)_ open `Security and Privacy` and give Accessibility and Screen Recording permissions to your terminal emulator - accessibility permission is for keybinds to work, screen recording to detect wheter Minecraft is the window in focus in order not to run macro somewhere random. - If you don't feel comfortable allowing Screen Recording, see **Optional steps** to disable checking actively focused window. Unfortunately, Accessibility permissions is required and I can't do anything with that.
5. Run `python3 main.py` in your terminal emulator. On Linux and MacOS you need to run `sudo python3 main.py` because of inner workings of `keyboard` module. Can't really do anything about that, if you don't feel comfortable doing so and feel like you know a better solution to adding hotkeys, please make Pull Request or create Issue with resources pointing me in that direction.
7. Start using macro. 🤷

# Additional steps

* If for whatever reason you don't want the macro to read actively focused window title (MacOS users might want to do that because of Screen Recording permission required in order to do so, Linux users might want to do that in case they're using Wayland composer and macro doesn't work there), change value of `check_minecraft_window_before_running_hotkey` in `config.ini` file to false. This requires setting `active_minecraft_version` to whatever major version you're running currently and restarting the macro, as checking version automatically is impossible in that case.
* In order to change keybinds, change their value in `config.ini`, under your platform section.
