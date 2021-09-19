from enum import Enum


class NotificationChannel:
    class ENUM(str, Enum):
        SMS = "SMS"
        WEB_PUSH = "WEB_PUSH"
        PUSH = "PUSH"
        EMAIL = "EMAIL"

    choices = (
        ("SMS", "SMS"),
        ("WEB_PUSH", "WEB_PUSH"),
        ("PUSH", "PUSH"),
        ("EMAIL", "EMAIL"),
    )


class NotificationType:
    class ENUM(str, Enum):
        TRANSACTIONAL = "TRANSACTIONAL"
        PROMOTIONAL = "PROMOTIONAL"

    choices = (
        ("TRANSACTIONAL", "TRANSACTIONAL"),
        ("PROMOTIONAL", "PROMOTIONAL"),
    )
