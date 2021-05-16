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
3. Navigate to unzipped/cloned folder in your terminal emulator and run `pip install -r requirements.txt`.
4. _(Additional step for MacOS)_ open `Security and Privacy` and give Accessibility and Screen Recording permissions to your terminal emulator - accessibility permission is for keybinds to work, screen recording to detect wheter Minecraft is the window in focus in order not to run macro somewhere random. - If you don't feel comfortable allowing Screen Recording, see **Optional steps** to disable checking actively focused window. Unfortunately, Accessibility permissions is required and I can't do anything with that.
5. Whlie in correct folder in your terminal emulator, run `python3 main.py`. In case you're trying to run on it Windows and your Python is correctly installed and has file associations, you can also just double click it. On Linux and MacOS you need to run `sudo python3 main.py` because of inner workings of `keyboard` module. Can't really do anything about that, if you don't feel comfortable doing so and feel like you know a better solution to adding hotkeys, please make Pull Request or create Issue with resources pointing me in that direction.
7. Start using macro. 🤷

## Optional steps

* In order to change keybinds, change their value in `config.ini` under your platform section - the names should be self-explanatory.
* If the macro is too fast, change `key_delay_in_miliseconds`  in `config.ini` to something higher, but I wouldn't really recommend anything more than 120.

*If you don't want to give Screen Recording permission on MacOS or macro doesn't work on Wayland:*

1. _(Optional step for Wayland users if Xlib fails to install - I don't know if it actually does, but it might 🤷)_ Remove `python-xlib==0.29; sys_platform == "linux"` line from `requirements.txt` and try to install them again.
2. Change `check_minecraft_window_before_running_hotkey` value to `false` in `config.ini`
3. Change `active_minecraft_version` in `config.ini` to whatever version you're currently running and restart macro. You have to do that every time you change version.
