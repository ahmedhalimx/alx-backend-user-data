#!/usr/bin/env python3
"Auth File"
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    hash a given password using bcrypt
    """
    return hashpw(password.encode(), gensalt())
