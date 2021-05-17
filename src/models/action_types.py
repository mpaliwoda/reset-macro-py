from enum import Enum


class ActionType(str, Enum):
    GENERATE_RSG_WORLD = "rsg"
    GENERATE_SSG_WORLD = "ssg"
    EXIT_WORLD = "exit"
    FORCE_PERCH = "perch"
