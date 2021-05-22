#!/bin/bash

options=(
    main.py
    --onedir
    --add-data config.ini:.
    --add-data logger.conf:.
    --add-data world_counter_1_14.txt:.
    --add-data world_counter_1_16.txt:.
)


[ -d "./dist" ] && rm -r "./dist"
[ -d "./build" ] && rm -r "./build"


if [ "$(uname)" == "Darwin" ]; then
    options+=(--hidden-import pyautogui --hidden-import AppKit --hidden-import Quartz)
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    options+=(--hidden-import pyautogui --hidden-import Xlib)
fi


pyinstaller ${options[@]}
