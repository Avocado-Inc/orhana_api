from enum import Enum


class OrderTransitionConstants:
    class ENUMS(str, Enum):
        PENDING = "PENDING"
        CONFIRMED = "CONFIRMED"
        TRANSIT = "TRANSIT"
        DELIVERED = "DELIVERED"

    choices = (
        ("PENDING", "PENDING"),
        ("CONFIRMED", "CONFIRMED"),
        ("TRANSIT", "TRANSIT"),
        ("DELIVERED", "DELIVERED"),
    )
