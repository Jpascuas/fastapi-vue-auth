import jwt
from users import get_users

SECRET = "secret123"


def authenticate(email, password):

    users = get_users()

    for user in users:
        if user["email"] == email and user["password"] == password:

            token = jwt.encode(
                {"email": user["email"]},
                SECRET,
                algorithm="HS256"
            )

            return token

    return None


def get_user_from_token(token):

    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
    users = get_users()

    for user in users:
        if user["email"] == payload["email"]:
            return user

    return None