from fastapi import status , HTTPException , Depends

from app.database import getDb
from sqlalchemy.orm.session import Session

from app.user.models import User
from app.utils.jwt import verify_token

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



# ----------------------------GET CURRENT USER-------------------------
def get_current_user(token:str = Depends(oauth2_scheme) , db:Session = Depends(getDb)):
    payload = verify_token(token)
    userId = payload["id"]

    user:User = db.query(User).filter(User.id == userId).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")

    return user
# ------------------------------------------------------------------


# ----------------------------GET CURRENT CUSTOMER-------------------------
def get_current_customer(user:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    if user.isAdmin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="not authorized")

    return user
# ------------------------------------------------------------------


# ----------------------------GET CURRENT ADMIN-------------------------
def get_current_admin(user:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    if not user.isAdmin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="not authorized")

    return user
# ------------------------------------------------------------------