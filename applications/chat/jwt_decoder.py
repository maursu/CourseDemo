import jwt
import os


def decode_user(token: str) -> str:
    """
    :param token: jwt token
    :return: username
    """
    decoded_data = jwt.decode(jwt=token,
                              key=os.getenv('SECRET_KEY'),
                              algorithms=["HS256"],
                              options={"verify_signature": False})

    return decoded_data['username']
