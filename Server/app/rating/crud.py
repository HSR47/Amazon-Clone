from sqlalchemy.orm import Session

import app.rating.models as ratingModel
import app.rating.schemas as ratingSchema

# ----------------------------RETRIEVE-------------------------
def get_rating_by_id(db: Session, rating_id: int):
    """
    Retrieves a rating from the database by its ID.

    Parameters:
        db (Session): The database session.
        rating_id (int): The ID of the rating to retrieve.

    Returns:
        ratingModel.Rating: The rating object with the specified ID.
    """
    rating = db.query(ratingModel.Rating).filter(ratingModel.Rating.id == rating_id).first()
    return rating

def get_rating_by_user_id_and_product_id(db: Session, user_id: int, product_id: int):
    """
    Retrieves the rating of a specific user for a specific product.

    Args:
        db (Session): The database session object.
        user_id (int): The ID of the user.
        product_id (int): The ID of the product.

    Returns:
        ratingModel.Rating: The rating object representing the user's rating for the product.
    """
    rating = db.query(ratingModel.Rating).filter((ratingModel.Rating.userId == user_id) & (ratingModel.Rating.productId == product_id)).first()
    return rating

def get_all_ratings_by_product_id(db: Session, product_id: int):
    """
    Retrieves all ratings for a given product ID from the database.

    Args:
        db (Session): The database session object.
        product_id (int): The ID of the product.

    Returns:
        List[ratingModel.Rating]: A list of ratingModel.Rating objects representing the ratings for the product.
    """
    ratings = db.query(ratingModel.Rating).filter(ratingModel.Rating.productId == product_id).all()
    return ratings

def get_all_ratings_by_user_id(db: Session, user_id: int):
    """
    Retrieves all ratings by user ID from the database.

    Parameters:
        db (Session): The database session object.
        user_id (int): The ID of the user.

    Returns:
        List[ratingModel.Rating]: A list of ratingModel.Rating objects representing the ratings by the user.
    """
    ratings = db.query(ratingModel.Rating).filter(ratingModel.Rating.userId == user_id).all()
    return ratings

def get_all_ratings(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves all ratings from the database.

    Parameters:
        db (Session): The database session to use.
        skip (int, optional): The number of ratings to skip. Defaults to 0.
        limit (int, optional): The maximum number of ratings to retrieve. Defaults to 100.

    Returns:
        List[ratingModel.Rating]: A list of ratingModel.Rating objects.
    """
    ratings = db.query(ratingModel.Rating).offset(skip).limit(limit).all()
    return ratings
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_rating(db:Session , user_id:int , product_id:int , data:ratingSchema.RatingCreate):
    """
    Creates a new rating in the database.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user creating the rating.
        product_id (int): The ID of the product being rated.
        data (ratingSchema.RatingCreate): The data for the new rating.

    Returns:
        ratingModel.Rating: The newly created rating object.
    """
    rating = ratingModel.Rating(
        userId = user_id,
        productId = product_id,
        star = data.star,
        comment = data.comment
    )

    db.add(rating)
    db.commit()
    db.refresh(rating)

    return rating
# ------------------------------------------------------------------


# ----------------------------UPDATE--------------------------
def update_rating(db:Session , rating:ratingModel.Rating , data:ratingSchema.RatingUpdate):
    """
    Update the rating with the given data.

    Args:
        db (Session): The database session.
        rating (ratingModel.Rating): The rating to be updated.
        data (ratingSchema.RatingUpdate): The data to update the rating with.

    Returns:
        ratingModel.Rating: The updated rating.
    """
    if data.star != None:
        rating.star = data.star

    if data.comment != None:
        rating.comment = data.comment
    
    db.commit()
    db.refresh(rating)

    return rating
# ------------------------------------------------------------------


# ----------------------------DELETE--------------------------
def delete_rating(db:Session , rating:ratingModel.Rating):
    """
    Delete the rating from the database.

    Args:
        db (Session): The database session.
        rating (ratingModel.Rating): The rating to be deleted.

    Returns:
        None
    """
    db.delete(rating)
    db.commit()
# ------------------------------------------------------------------