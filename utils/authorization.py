from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from utils.config import authorization_list

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


def verify_token(token: str = Depends(oauth2_scheme)):
    if not token:
        return None
    if not authorization_list or token in authorization_list:
        return token
    elif token.startswith("eyJhbGciOi"):
        return token
    else:
        raise HTTPException(status_code=401, detail="Not authenticated")
