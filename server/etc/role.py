ROLE_MUTED = 'muted'
ROLE_USER = 'user'
ROLE_MODER = 'moder'
ROLE_ADMIN = 'admin'

ROLE_IERARCHY = [
    ROLE_MUTED,
    ROLE_USER,
    ROLE_MODER,
    ROLE_ADMIN,
]

def role_is_muted(role: str) -> bool: return role == ROLE_MUTED
def role_is_user(role: str) -> bool: return role == ROLE_USER or role == ROLE_MODER or role == ROLE_ADMIN
def role_is_moder(role: str) -> bool: return role == ROLE_MODER or role == ROLE_ADMIN
def role_is_admin(role: str) -> bool: return role == ROLE_ADMIN