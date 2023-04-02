"""
Auth logic
"""
import hashlib
from notebook import Notebook


class AuthException(Exception):
    """
    Exeption in auth
    """

    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    """
    Username already exist exeption
    """

    def __str__(self) -> str:
        return f"User with {self.username} already exist."


class PasswordTooShort(AuthException):
    """
    Password too short exeption
    """

    def __str__(self) -> str:
        return f"Too short password for {self.username}."


class InvalidUsername(AuthException):
    """
    Invalid username exeption
    """

    def __str__(self) -> str:
        return f"Invalid username: {self.username}."


class InvalidPassword(AuthException):
    """
    Invalid password exeption
    """

    def __str__(self) -> str:
        return f"Invalid password for {self.username}."


class PermissionError(Exception):
    """
    Permision denied error
    """

    def __init__(self, message, *args: object) -> None:
        self.message = message
        super().__init__(*args)

    def __str__(self) -> str:
        return self.message


class NotLoggedInError(AuthException):
    """
    Not logged in error
    """

    def __str__(self) -> str:
        return f"User {self.username} is not logged in"


class NotPermittedError(AuthException):
    """
    Not permited eaxeption
    """

    def __str__(self) -> str:
        return f"User {self.username} is not permitted."


class User:
    """
    Class User
    """

    def __init__(self, username, password):
        """Create a new user object. The password
        will be encrypted before storing."""
        self.username = username
        self.password = self._encrypt_pw(password)
        self.notebook = Notebook()

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this
        user, false otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    """
    Class Authenticator
    """

    def __init__(self):
        """Construct an authenticator to manage
        users logging in and out."""
        self.users = {}

    def add_user(self, username, password):
        """
        Add user method
        """
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        """
        Logging in method
        """
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username, user)
        return user


class Authorizor:
    """
    Class Authorizor
    """

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """Create a new permission that users
        can be added to"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """
        Checks permission
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True
