
import cloudinary
from cloudinary import uploader
from app.config import settings
          
cloudinary.config( 
  cloud_name = settings.CLOUDINARY_NAME, 
  api_key = settings.CLOUDINARY_KEY, 
  api_secret = settings.CLOUDINARY_SECRET 
)

def uploadImage(file):
    upload_params = {
        "transformation": [ {"quality": "auto:low"}, ]
    }
    response = uploader.upload(file, **upload_params)
    return response["secure_url"] , response["public_id"]

def deleteImage(publicId):
    result = uploader.destroy(public_id=publicId)
    return result["result"] == "ok"