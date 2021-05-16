from enum import Enum


class Action(str, Enum):
    GENERATE_RSG_WORLD = "rsg"
    GENERATE_SSG_WORLD = "ssg"
    EXIT_WORLD = "exit"
