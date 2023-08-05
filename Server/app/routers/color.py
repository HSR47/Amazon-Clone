
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.brandModel import Brand
from app.models.colorModel import Color

from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_user
import app.schemas.brandSchema as brandSchema
from app.schemas.colorSchema import addColorRequest, returnColor, updateColorRequest

colorRouter = APIRouter(tags=["Color"])

# ----------------------------ADD COLOR-------------------------
@colorRouter.post("/color" , response_model=returnColor)
def add_color(data:addColorRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    check = db.query(Color).filter(Color.name == data.name).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="color already exists")
    
    color = Color(
        name = data.name
    )

    db.add(color)
    db.commit()
    db.refresh(color)

    return color
# ------------------------------------------------------------------


# ----------------------------GET ALL COLORS-------------------------
@colorRouter.get("/color" , response_model=list[returnColor])
def get_all_colors(curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    allColors = db.query(Color).all()
    return allColors
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC COLOR-------------------------
@colorRouter.get("/color/{id}" , response_model=returnColor)
def get_specific_color(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    color = db.query(Color).filter(Color.id == id).first()
    if color == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="color not found")
    
    return color
# ------------------------------------------------------------------


# ----------------------------UPDATE COLOR-------------------------
@colorRouter.put("/color/{id}")
def update_color(id:int , data:updateColorRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    
    color:Color = db.query(Color).filter(Color.id == id).first()
    if color == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="color not found")   

    if data.name == None:
        return color
    
    check = db.query(Color).filter(Color.name == data.name).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="color already exists")

    color.name = data.name
    db.commit()
    
    return {"message" : "updated"}
# ------------------------------------------------------------------


# ----------------------------DELETE COLOR-------------------------
@colorRouter.delete("/color/{id}")
def delete_color(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    color:Color = db.query(Color).filter(Color.id == id).first()
    if color == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="color not found")  
    
    db.delete(color)
    db.commit()

    return {"message" : "deleted"}
# ------------------------------------------------------------------