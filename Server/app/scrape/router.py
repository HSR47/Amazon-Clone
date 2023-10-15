
from fastapi import APIRouter , Depends
from slugify import slugify
from app.utils.scrape import scrapeData
from app.brand.models import Brand
from app.category.models import ProdCategory
from app.image.models import ProductImage
from app.product.models import Product
from app.scrape.schemas import scrapeRequest

from app.database import getDb
from sqlalchemy.orm.session import Session

from app.user.models import User
from app.auth.dependencies import get_current_admin

scrapeRouter = APIRouter(tags=["Scrape"])


@scrapeRouter.post("/scrape")
def scrape(data:scrapeRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    print("--------------------------SCRAPING DATA--------------------------")
    
    cat = data.category
    maxPage = data.maxPage

    # ----------------------------CATEGORY-------------------------
    category = db.query(ProdCategory).filter(ProdCategory.name == cat).first()
    if category == None:
        newCategory = ProdCategory(
            name = cat,
        )
        db.add(newCategory)
        db.commit()
        db.refresh(newCategory)
        category = newCategory
        
        print("New category added")
    
    else:
        print("Category already exists")
    # ------------------------------------------------------------------


    data = scrapeData(category=cat , maxPages=maxPage)         # SCRAPING HERE
    for i in data:

        # ----------------------------SLUG-------------------------
        slug = slugify(i['title'])
        checkSlug = db.query(Product).filter(Product.slug == slug).first()
        if checkSlug != None:
            print(f"{slug} already exists")
            continue
        # ------------------------------------------------------------------


        # ----------------------------BRAND-------------------------
        brandName:str = i['title'].split()[0]
        brand = db.query(Brand).filter(Brand.name == brandName).first()
        if brand == None:
            newBrand = Brand(
                name = brandName,
            )
            db.add(newBrand)
            db.commit()
            db.refresh(newBrand)
            brand = newBrand
            print(f"new brand {brandName} added")
        # ------------------------------------------------------------------


        # ----------------------------PRODUCT-------------------------
        newProduct = Product(
            title = i['title'],
            slug = slug,
            description = i['description'],
            price = i['price'],
            quantity = 50,
            brandId = brand.id,
            categoryId = category.id
        )

        db.add(newProduct)
        db.commit()
        db.refresh(newProduct)
        print("new product added")
        # ------------------------------------------------------------------


        # ----------------------------IMAGES-------------------------
        for imgUrl in i['images']:
            image = ProductImage(
                productId = newProduct.id,
                name = 'NA',
                url = imgUrl,
                publicId = "NA" 
            )
            db.add(image)

            print("image added for previously added product")
        # ------------------------------------------------------------------

        db.commit()

    print("--------------------------DATABASE FILLED--------------------------")

    return {'message' : 'scraped successfully'}
