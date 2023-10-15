from fastapi import status , HTTPException
from jose import jwt , JWTError
from app.config import settings
from datetime import datetime , timedelta


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_MINUTES = settings.REFRESH_TOKEN_EXPIRE_MINUTES


# ----------------------------CREATE ACCESS TOKEN-------------------------
def create_access_token(data : dict = {}):
    toEncode = data.copy()
    toEncode["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    encoded_jwt = jwt.encode(toEncode , SECRET_KEY , algorithm=ALGORITHM)

    return encoded_jwt
# ------------------------------------------------------------------


# ----------------------------CREATE REFRESH TOKEN-------------------------
def create_refresh_token(data : dict = {}):
    toEncode = data.copy()
    toEncode["exp"] = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    encoded_jwt = jwt.encode(toEncode , SECRET_KEY , algorithm=ALGORITHM)

    return encoded_jwt
# ------------------------------------------------------------------


# ----------------------------VERIFY TOKEN-------------------------
def verify_token(token : str):
    try:
        return jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")
    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="unknown error occured")
# ------------------------------------------------------------------
