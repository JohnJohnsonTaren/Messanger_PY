class MessengerError(Exception): pass
class ValidationError(MessengerError):pass
class EmptyUsernameError(ValidationError):pass
class UserAlreadyExistsError(ValidationError):pass
class WeakPasswordError(ValidationError):pass
class AuthError(MessengerError):pass
class InvalidCredentialsError(AuthError):pass
