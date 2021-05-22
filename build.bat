@ECHO off
@RD /S /Q .\main.build
@RD /S /Q .\main.dist

python -m nuitka ^
    --assume-yes-for-downloads ^
    --include-package=win32 ^
    --include-data-file=config.ini=config.init ^
    --include-data-file=logger.conf=logger.conf ^
    --include-data-file=world_counter_1_14.txt=world_counter_1_14.txt ^
    --include-data-file=world_counter_1_16.txt=world_counter_1_16.txt ^
    --standalone .\main.py
pause
