#!/usr/bin/env python3
"Auth File"
from db import DB
from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound
from user import User


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, str(hashed_password))
            return user
        else:
            raise ValueError(f"User {email} already exists")


def _hash_password(password: str) -> bytes:
    """
    hash a given password using bcrypt
    """
    return hashpw(password.encode(), gensalt())
