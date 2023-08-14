
from fastapi import Depends
from slugify import slugify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.imageModel import ProductImage
from app.models.brandModel import Brand
from app.models.productModel import Product
from app.utils.scrapy import scrapeData
from app.config import settings
from sqlalchemy.orm.session import Session
from app.models.categoryModel import ProdCategory

URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}/{settings.DB_DB}"

engine = create_engine(url=URL)

SessionLocal = sessionmaker(autoflush=False , autocommit=False , bind=engine)
    
def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def fillDatabase(cats):
    print("filling database")
    db = SessionLocal()
    
    for cat in cats:
        category = db.query(ProdCategory).filter(ProdCategory.name == cat).first()
        if category == None:
            newCategory = ProdCategory(
                name = cat,
            )
            db.add(newCategory)
            db.commit()
            db.refresh(newCategory)
            category = newCategory
        
        data = scrapeData(category=cat , maxPages=5)         # SCRAPING HERE
        for i in data:
            slug = slugify(i['title'])
            checkSlug = db.query(Product).filter(Product.slug == slug).first()
            if checkSlug != None:
                continue

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

            image = ProductImage(
                productId = newProduct.id,
                name = i['imgAlt'],
                url = i['imgUrl'],
                publicId = "NA" 
            )

            db.add(image)
            db.commit()
            



    print("database filled")

    db.close()
