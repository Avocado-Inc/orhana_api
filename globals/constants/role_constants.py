from enum import Enum


class RoleConstants:
    class ENUMS(str, Enum):
        CUSTOMER = "CUSTOMER"
        SELLER = "SELLER"

    choices = (("CUSTOMER", "CUSTOMER"), ("SELLER", "SELLER"))
