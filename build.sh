#!/bin/bash

options=(
    -m nuitka
    --assume-yes-for-downloads
    --standalone main.py
    --include-data-file=config.ini=config.ini
    --include-data-file=logger.conf=logger.conf
    --include-data-file=world_counter_1_14.txt=world_counter_1_14.txt
    --include-data-file=world_counter_1_16.txt=world_counter_1_16.txt 
)

[ -d "./main.build" ] && rm -r "./main.build"
[ -d "./main.dist" ] && rm -r "./main.dist"


if [ "$(uname)" == "Darwin" ]; then
    options+=(--include-package=pyautogui --include-package=AppKit --include-package=Quartz)
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    options+=(--include-package=pyautogui --include-package=Xlib)
fi


if command -v python3 >/dev/null 2>&1; then
    python3 ${options[@]}
elif command -v python3 >/dev/null 2>&1; then
    python ${options[@]}
else
    printf "Python is not installed"
fi
