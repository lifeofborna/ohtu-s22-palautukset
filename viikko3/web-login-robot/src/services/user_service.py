from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise Exception(
                f"User with username {username} is too short!"
            )

        if len(password) < 3:
            raise Exception(
                f"Password should more than 3 values"
            )
        
        if (re.match("^[a-z]+$", f"{username}")) == False:
            raise Exception(
                f"Username should be only letters! "
            )

        if password != password_confirmation:
            raise Exception(
                f"check conf"
            )

user_service = UserService()
