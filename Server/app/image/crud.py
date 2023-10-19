from fastapi import UploadFile
from sqlalchemy.orm import Session

import app.image.models as imgModel
import app.image.schemas as imgSchema

from app.utils.cloudinary import deleteImage, uploadImage

# ----------------------------RETRIEVE-------------------------
def get_image_by_id(db:Session , image_id:int):
    image = db.query(imgModel.ProductImage).filter(imgModel.ProductImage.id == image_id).first()
    return image

def get_all_images_by_product_id(db:Session , product_id:int):
    allImages = db.query(imgModel.ProductImage).filter(imgModel.ProductImage.productId == product_id).all()
    return allImages

def get_all_images(db:Session):
    allImages = db.query(imgModel.ProductImage).all()
    return allImages

def get_thumbnail_of_a_product(db:Session , product_id:int):
    thumbnail = db.query(imgModel.ProductImage).filter(imgModel.ProductImage.thumbnail == True).first()
    return thumbnail
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_image(db:Session , data:imgSchema.ImageCreate , img:UploadFile):
    url , publicId = uploadImage(img.file)
    
    newImage = imgModel.ProductImage(
        productId = data.productId,
        name = img.filename,
        url = url,
        publicId = publicId
    )

    if data.thumbnail == True:
        currentThumbnail = get_thumbnail_of_a_product(db , data.productId)
        if currentThumbnail != None:
            currentThumbnail.thumbnail = False
        newImage.thumbnail = True

    db.add(newImage)
    db.commit()
    db.refresh(newImage)

    return newImage
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_image(db:Session , image:imgModel.ProductImage):
    deleteImage(image.publicId)
    db.delete(image)
    db.commit()
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_thumbnail(db:Session , image:imgModel.ProductImage):
    currentThumbnail = get_thumbnail_of_a_product(db, image.productId)

    if currentThumbnail != None:
        currentThumbnail.thumbnail = False
    
    image.thumbnail = True

    db.commit()
    db.refresh(image)

    return image
# ------------------------------------------------------------------