from typing import Annotated
from fastapi import APIRouter, Form , HTTPException , status , Depends , UploadFile
from sqlalchemy.orm import Session
from app.database import getDb

import app.product.models as prodModel
import app.product.crud as prodCrud
import app.auth.dependencies as authDep
import app.user.models as userModel
import app.image.schemas as imgSchema
import app.image.crud as imgCrud
import app.image.dependencies as imgDep
import app.image.models as imgModel



imageRouter = APIRouter(tags=["Product Image"])


# ----------------------------ADD IMAGE-------------------------
@imageRouter.post("/product/image" , response_model=imgSchema.ImageReturn)
def add_image(
    *,
    productId: Annotated[int , Form()],
    thumbnail: Annotated[bool , Form()] = False,
    image:UploadFile,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)],
):
    product:prodModel.Product = prodCrud.get_product_by_id(db , productId)
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")

    data = imgSchema.ImageCreate(
        productId=productId,
        thumbnail=thumbnail
    )

    try:
        newImage = imgCrud.create_image(db , data , image)
        return newImage
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="unexpected error occured")
# ------------------------------------------------------------------


# ----------------------------REMOVE IMAGE-------------------------
@imageRouter.delete("/product/image/{image_id}")
def remove_image(
    *,
    image:Annotated[imgModel.ProductImage , Depends(imgDep.valid_image_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    imgCrud.delete_image(db , image)

    return {"message" : "removed"}
# ------------------------------------------------------------------


# ----------------------------CHANGE THUMBNAIL-------------------------
@imageRouter.patch("/product/image/{image_id}/thumbnail" , response_model=imgSchema.ImageReturn)
def change_thumbnail(
    *,
    image:Annotated[imgModel.ProductImage , Depends(imgDep.valid_image_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    updatedImage = imgCrud.update_thumbnail(db , image)
    return updatedImage
# ------------------------------------------------------------------