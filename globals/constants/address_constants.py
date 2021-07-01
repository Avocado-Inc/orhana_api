from enum import Enum


class AddressTypeConstants:
    class ENUMS(str, Enum):
        WORK = "WORK"
        HOME = "HOME"
        OTHER = "OTHER"

    choices = (("WORK", "WORK"), ("HOME", "HOME"), ("OTHER", "OTHER"))
