from enum import Enum


class Role(Enum):
    muted = "muted"
    default = "default"
    moderator = "moderator"
    admin = "admin"
